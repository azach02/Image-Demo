from images import Image

def main():
    fileName = input("Please enter the file name that you wish to use. \n(MUST be a .gif file): ")
    
    try:
        myImage = Image(fileName)
        print("Close the Image window to continue.")
        blackAndWhite(myImage)
        myImage.draw()  # Display the black and white image
    except Exception as e:
        print(f"Error: {e}")

def blackAndWhite(image):
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)

    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)

if __name__ == "__main__":
    main()
