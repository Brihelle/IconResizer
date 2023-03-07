import glob
from PIL import Image

AndroidIconSizes = [36,48,72,96]
iOSIconSizes = [20,29, 40,58, 60, 57,72,76,87,114,120,144,152,167,180,1024]

def generateAndroidIcons(image):
    for size in AndroidIconSizes:
        outFilePath = "output/android/"+str(size) + "x" + str(size)+".png"
        resizedImage = image.resize((size, size), Image.ANTIALIAS)
        resizedImage.save(outFilePath,"PNG")

def generateIosIcons(image):
    for size in iOSIconSizes:
        outFilePath = "output/iOS/"+str(size) + "x" + str(size)+".png"
        resizedImage = image.resize((size, size), Image.ANTIALIAS)
        resizedImage.save(outFilePath,"PNG")

def generateIcons():
    print(glob.glob("input/*.png"))
    iconPathsArray = glob.glob("input/*.png")
    for iconPath in iconPathsArray:
        with Image.open(iconPath) as image:
            generateAndroidIcons(image)
            generateIosIcons(image)

generateIcons()