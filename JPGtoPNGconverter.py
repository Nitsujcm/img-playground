# python JPGtoPNGconverter.py Pokedex\ new\
# create new folder

import sys
from pathlib import Path
from PIL import Image

# grab the 1st and 2nd argument
source_folder = Path(f'./{sys.argv[1]}')
dest_folder = Path(f'./{sys.argv[2]}')

# check if new folder exists, if not, create it
if not dest_folder.exists():
    dest_folder.mkdir()

# loop through Pokedex and convert to PNG
for f in source_folder.iterdir():
    dfn, e = str(f).split('.')
    _, fn = dfn.split('\\')
    with Image.open(f) as img:
        outfile = '.\\' + str(dest_folder) + '\\' + fn + '.png'
        img.save(outfile, 'png')


# Save to new folder
