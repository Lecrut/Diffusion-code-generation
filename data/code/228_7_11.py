from PIL import Image

def create_colored_triangle():
    width = 200
    height = 200
    image = Image.new('RGB', (width, height), 'white')
    pixels = image.load()
    for x in range(width):
        for y in range(height):
            if y <= x:
                pixels[x, y] = (255, 0, 0)
            else:
                pixels[x, y] = (255, 255, 255)
    return image
if __name__ == '__main__':
    triangle_image = create_colored_triangle()
    triangle_image.show()