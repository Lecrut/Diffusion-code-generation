from PIL import Image

class TriangleImage:
    WIDTH = 200
    HEIGHT = 200
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    @staticmethod
    def create_triangle_image():
        image = Image.new('RGB', (TriangleImage.WIDTH, TriangleImage.HEIGHT), 'white')
        pixels = image.load()
        
        for y in range(TriangleImage.HEIGHT):
            for x in range(y + 1):
                if x <= y:
                    pixels[x, y] = TriangleImage.RED
                else:
                    pixels[x, y] = TriangleImage.GREEN
        
        return image

if __name__ == '__main__':
    triangle_image = TriangleImage.create_triangle_image()
    triangle_image.show()