from PIL import Image, ImageDraw

def create_blue_box():
    img = Image.new('RGB', (250, 250), color = (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, 200, 200], fill=(0, 0, 255))
    return img

if __name__ == '__main__':
    blue_box_image = create_blue_box()
    blue_box_image.show()