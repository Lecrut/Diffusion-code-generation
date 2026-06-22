from PIL import Image, ImageDraw

class RedTriangle:
    def __init__(self, width=200, height=200):
        self.width = width
        self.height = height
        self.background_color = 'white'
        self.triangle_points = [(50, 150), (150, 50), (250, 150)]
        self.image = Image.new('RGB', (self.width, self.height), self.background_color)
        self.draw = ImageDraw.Draw(self.image)

    def draw_triangle(self):
        self.draw.polygon(self.triangle_points, fill='red')

    def save_image(self, filename):
        self.image.save(filename)

if __name__ == '__main__':
    red_triangle = RedTriangle()
    red_triangle.draw_triangle()
    red_triangle.save_image('red_triangle.png')