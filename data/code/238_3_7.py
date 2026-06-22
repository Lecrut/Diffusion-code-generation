from PIL import Image, ImageDraw

def create_box_image():
    width = 210
    height = 210
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.rectangle([10, 10, 200, 200], fill=(0, 0, 255))
    return image

if __name__ == '__main__':
    box_image = create_box_image()
    box_image.show()