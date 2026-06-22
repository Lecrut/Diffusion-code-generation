from PIL import Image, ImageDraw

class BoxDrawer:
    def __init__(self):
        self.width = 300
        self.height = 300
        self.box_color = (0, 0, 255)

    @staticmethod
    def create_image(width, height):
        return Image.new('RGB', (width, height), color=(255, 255, 255))

    def draw_box(self, image, box_color):
        draw = ImageDraw.Draw(image)
        draw.rectangle([10, 10, 200, 200], outline=box_color)

    def get_image(self):
        image = self.create_image(self.width, self.height)
        self.draw_box(image, self.box_color)
        return image

if __name__ == '__main__':
    drawer = BoxDrawer()
    image = drawer.get_image()
    image.show()