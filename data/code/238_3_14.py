from PIL import Image, ImageDraw

def create_box_image(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Invalid dimensions")
    
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)
    draw.rectangle([10, 10, 200, 200], fill=(0, 0, 255))
    return image

if __name__ == '__main__':
    box_width = 300
    box_height = 300
    image = create_box_image(box_width, box_height)
    image.show()