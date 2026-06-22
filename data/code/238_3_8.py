from PIL import Image, ImageDraw

def create_colored_image():
    img = Image.new('RGB', (256, 256), color = (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle((10, 10, 200, 200), fill=(0, 0, 255))
    return img

if __name__ == '__main__':
    image = create_colored_image()
    image.show()