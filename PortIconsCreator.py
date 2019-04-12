from PIL import Image
from PIL import ImageOps
from random import randrange

# TODO:
# 1- Refactor
# 2- Crop smaller icon from 20x20 to like 20x16 (width is currently or, high has too much margin)
# 3- Paste over so we still see a white background on the larger images
# 4- Put a black line around the large image

IconIm = Image.open('PortIcon.png')

#image = Image.open('test.png')
new_White_image = Image.new("RGBA", (240, 30), "WHITE")    # Create a white rgba background
#image = Image.open('test.png')
new_RED_image = Image.new("RGBA", IconIm.size, "RED")    # Create a white rgba background
new_RED_image.paste(IconIm, (0, 0), IconIm)              # Paste the image on the background. Go to the links given below for details.
#new_image.convert('RGB').save('test.jpg', "JPEG")    # Save as JPEG
new_GREEN_image = Image.new("RGBA", IconIm.size, "GREEN")    # Create a white rgba background
new_GREEN_image.paste(IconIm, (0, 0), IconIm)

RedIconImSmall = new_RED_image.copy()
RedIconImSmall = new_RED_image.resize((20, 15))
GreenIconImSmall = new_GREEN_image.copy()
GreenIconImSmall = new_GREEN_image.resize((20, 15))


IconImLarge = new_White_image.copy()
IconImLarge = new_White_image.resize((240, 30))


portWidth = 20
portHeight = 15

RedIconCopy = RedIconImSmall.copy()
GreenIconCopy = GreenIconImSmall.copy()
j = 1
for i in range(0,240,portWidth):
    j += 1
    for top in range(0,30,portHeight):
        print(i,top)
        print(j)
        myInt = randrange(24)
        if myInt % 2 == 0:
        #if j % 2 == 0:
            IconImLarge.paste(RedIconCopy,(i,top))
        else:
            #None
            IconImLarge.paste(GreenIconCopy, (i, top))


IconImLarge.save('Output33.png')

#rgb_im = IconImLarge.convert('RGB')
#rgb_im.save('OutputJPGv1.jpg')

