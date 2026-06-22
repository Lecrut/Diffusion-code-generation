from PIL import Image, ImageDraw

def create_colored_right_triangle(width, height, fill_color):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be greater than zero.")
    
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)
    
    triangle_points = [(0, height), (width, 0), (width, height)]
    draw.polygon(triangle_points, fill=fill_color)
    
    return image

if __name__ == '__main__':
    width = 100
    height = 150
    fill_color = 'red'
    triangle_image = create_colored_right_triangle(width, height, fill_color)
    triangle_image.save('colored_triangle.png')