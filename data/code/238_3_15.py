from PIL import Image, ImageDraw

def create_blue_box():
    width = 210
    height = 210
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    box = [(10, 10), (200, 200)]
    draw.rectangle(box, fill='blue')
    return image

if __name__ == '__main__':
    blue_box_image = create_blue_box()
    blue_box_image.show()