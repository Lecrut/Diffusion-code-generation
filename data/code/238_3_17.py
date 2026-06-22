from PIL import Image, ImageDraw

def create_filled_box_image():
    img = Image.new('RGB', (256, 256), color = (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, 200, 200], fill=(0, 0, 255))
    return img

if __name__ == '__main__':
    image = create_filled_box_image()
    image.show()