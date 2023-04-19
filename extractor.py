# --------- Opcion 1


import re
from pdfminer.high_level import extract_pages,extract_text

for page_layout in extract_pages("./tu.pdf"):
    for element in page_layout:
        print(element)


# --------- Opcion 2 -------------

text = extract_text("./tu.pdf")
print(text)

patter = re.compile(r"[a-Za-Z]+,{1}\s{1}")
matches = patter.findall(text)
names = [n[:-2] for n in matches]
print(names)

# --------- extrac imagenes
import fitz
import PIL.Image
import io


pdf = fitz.open("./tu.pdf")
counter = 1

for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in images:
        base_img = pdf.extract_image(image[0])
        image_data = base_img["image"]
        img = PIL.Image.open(io.BytesIO(image_data))
        Extension = base_img['ext']
        img.save(open(f"image{counter}.{Extension}","wb"))
        counter += 1






