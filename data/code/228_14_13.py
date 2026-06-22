from PIL import Image, ImageDraw

class RedTriangle:
    def __init__(self):
        self.width = 200
        self.height = 200
        self.background_color = 'white'
        self.triangle_points = [(50, 150), (150, 50), (250, 150)]

    def create_image(self):
        image = Image.new('RGB', (self.width, self.height), self.background_color)
        draw = ImageDraw.Draw(image)
        draw.polygon(self.triangle_points, fill='red')
        return image

if __name__ == '__main__':
    red_triangle = RedTriangle()
    image = red_triangle.create_image()
    image.save('red_triangle.png')