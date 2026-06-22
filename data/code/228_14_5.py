from PIL import Image, ImageDraw

class RedTriangleGenerator:
    WIDTH = 200
    HEIGHT = 200
    BACKGROUND_COLOR = 'white'
    TRIANGLE_POINTS = [(50, 150), (150, 50), (250, 150)]
    FILL_COLOR = 'red'

    @staticmethod
    def create_red_triangle():
        image = Image.new('RGB', (RedTriangleGenerator.WIDTH, RedTriangleGenerator.HEIGHT), RedTriangleGenerator.BACKGROUND_COLOR)
        draw = ImageDraw.Draw(image)
        draw.polygon(RedTriangleGenerator.TRIANGLE_POINTS, fill=RedTriangleGenerator.FILL_COLOR)
        return image

if __name__ == '__main__':
    red_triangle_image = RedTriangleGenerator.create_red_triangle()
    red_triangle_image.save('red_triangle.png')