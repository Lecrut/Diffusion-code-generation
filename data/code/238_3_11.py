from PIL import Image, ImageDraw

def create_blue_box(width=300, height=300):
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    box_coords = [(10, 10), (200, 200)]
    fill_color = (0, 0, 255)
    draw.rectangle(box_coords, outline=None, fill=fill_color)
    return image

if __name__ == '__main__':
    sample_image = create_blue_box(300, 300)
    sample_image.show()