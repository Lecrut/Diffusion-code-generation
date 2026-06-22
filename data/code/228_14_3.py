from PIL import Image, ImageDraw

def create_red_triangle():
    width, height = 200, 200
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    points = [(50, 150), (150, 150), (100, 50)]
    draw.polygon(points, fill='red')
    return image

if __name__ == '__main__':
    image = create_red_triangle()
    image.save('red_triangle.png')