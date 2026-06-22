from PIL import Image, ImageDraw

def create_red_triangle():
    dimensions = {'width': 200, 'height': 200}
    colors = {'red': (255, 0, 0), 'white': (255, 255, 255)}
    
    image = Image.new('RGB', (dimensions['width'], dimensions['height']), colors['white'])
    draw = ImageDraw.Draw(image)
    points = [(50, 150), (150, 50), (250, 150)]
    draw.polygon(points, fill=colors['red'])
    
    return image

if __name__ == '__main__':
    red_triangle_image = create_red_triangle()
    red_triangle_image.save('red_triangle.png')