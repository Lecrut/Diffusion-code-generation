from PIL import Image, ImageDraw

def create_red_triangle():
    width, height = 200, 200
    background_color = 'white'
    triangle_points = [(50, 150), (150, 50), (250, 150)]
    
    validate_dimensions(width, height)
    validate_triangle_points(triangle_points)
    
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)
    draw.polygon(triangle_points, fill='red')
    return image

def validate_dimensions(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers")

def validate_triangle_points(points):
    if len(points) != 3:
        raise ValueError("Triangle points must consist of exactly three coordinates")
    for point in points:
        if len(point) != 2:
            raise ValueError("Each triangle point must have two coordinates")

if __name__ == '__main__':
    red_triangle_image = create_red_triangle()
    red_triangle_image.save('red_triangle.png')