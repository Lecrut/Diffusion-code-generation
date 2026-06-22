from PIL import Image, ImageDraw

def draw_red_triangle():
    width, height = 300, 200
    background_color = 'white'
    triangle_points = [(100, 150), (200, 50), (300, 150)]
    
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)
    draw.polygon(triangle_points, fill='red')
    
    return image

if __name__ == '__main__':
    red_triangle_image = draw_red_triangle()
    red_triangle_image.save('red_triangle.png')