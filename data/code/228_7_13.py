from PIL import Image

class ColoredRightAngledTriangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new('RGB', (width, height), color=(255, 255, 255))

    def draw_triangle(self, x1, y1, x2, y2, x3, y3, fill_color):
        pixels = self.image.load()
        for y in range(y1, y3 + 1):
            for x in range(x1, x2 + 1):
                if (x - x1) * (y - y2) == (x2 - x1) * (y - y1):
                    pixels[x, y] = fill_color

    def save_image(self, filename):
        self.image.save(filename)

if __name__ == '__main__':
    triangle = ColoredRightAngledTriangle(200, 200)
    triangle.draw_triangle(50, 150, 150, 150, 100, 50, (255, 0, 0))
    triangle.save_image('colored_right_angled_triangle.png')