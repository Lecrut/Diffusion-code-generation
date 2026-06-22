from PIL import Image, ImageDraw

def create_red_triangle():
    img = Image.new('RGB', (200, 200), 'white')
    draw = ImageDraw.Draw(img)
    points = [(50, 150), (150, 50), (250, 150)]
    draw.polygon(points, fill='red')
    img.save('red_triangle.png')

if __name__ == '__main__':
    create_red_triangle()