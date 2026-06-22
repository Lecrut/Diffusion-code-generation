from PIL import Image, ImageDraw
WIDTH = 200
HEIGHT = 200
BACKGROUND_COLOR = 'white'
TRIANGLE_POINTS = [(50, 150), (150, 50), (250, 150)]
FILL_COLOR = 'red'

def create_red_triangle():
    image = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)
    draw.polygon(TRIANGLE_POINTS, fill=FILL_COLOR)
    return image
if __name__ == '__main__':
    red_triangle_image = create_red_triangle()
    red_triangle_image.save('red_triangle.png')