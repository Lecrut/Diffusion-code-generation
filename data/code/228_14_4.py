from PIL import Image, ImageDraw

def create_red_triangle():
    width, height = 200, 200
    background_color = 'white'
    triangle_points = [(50, 150), (150, 50), (250, 150)]
    
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)
    draw.polygon(triangle_points, fill='red')
    
    return image

if __name__ == '__main__':
    red_triangle_image = create_red_triangle()
    red_triangle_image.save('red_triangle.png')