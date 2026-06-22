from PIL import Image, ImageDraw

class ImageDrawer:
    def __init__(self, width=200, height=200):
        self.width = width
        self.height = height
        self.background_color = 'white'
        self.triangle_points = [(50, 150), (150, 50), (250, 150)]
    
    def create_image(self):
        image = Image.new('RGB', (self.width, self.height), self.background_color)
        draw = ImageDraw.Draw(image)
        draw.polygon(self.triangle_points, fill='red')
        return image
    
    def save_image(self, filename):
        self.create_image().save(filename)

if __name__ == '__main__':
    drawer = ImageDrawer()
    drawer.save_image('red_triangle.png')