from PIL import Image, ImageDraw

def create_blue_box():
    width = 300
    height = 300
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.rectangle([10, 10, 200, 200], fill=(0, 0, 255))
    return image

if __name__ == '__main__':
    blue_box_image = create_blue_box()
    blue_box_image.show()