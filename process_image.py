import os
from PIL import Image

input_dir = 'images'
output_dir = 'new_images'

for infile in os.listdir(input_dir):
    inpath = os.path.join(input_dir, infile)
    im = Image.open(inpath)
    new_im = im.rotate(-90).resize((128,128)).convert('RGB')

    file, ext = os.path.splitext(infile)
    outpath = os.path.join(output_dir, file + '.jpg')
    new_im.save(outpath, "JPEG")
