from PIL import Image, ImageDraw

def create_blue_box():
    width, height = 210, 210
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    box_coords = [(10, 10), (200, 200)]
    draw.rectangle(box_coords, fill='blue')
    return img

if __name__ == '__main__':
    image = create_blue_box()
    print(image)