##############################
# This script is useful for rotating images based on any rotation stored in 
# their EXIF data, which is common in iOS.
# NOTE - this removes other EXIF information like date taken
##############################
from PIL import Image, ExifTags
import glob
import os.path

files = glob.glob('~/my_photos/*.jpg')
count = 0
for file in files:
    try:
        image = Image.open(file)
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = dict(image._getexif().items())

        rot = 0
        if exif[orientation] == 3:
            rot = 180
        elif exif[orientation] == 6:
            rot = 270
        elif exif[orientation] == 8:
            rot = 90
        
        if rot != 0:
            image = image.rotate(rot, expand=True)
            print('Rotated "' + os.path.basename(file) + '" by ' + str(rot) + ' degrees')
            count = count + 1
            image.save(file)
            image.close()

    except (AttributeError, KeyError, IndexError):
        pass  # image didn't have getexif

print('Finished! Rotated ' + str(count) + ' images.')
