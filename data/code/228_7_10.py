from PIL import Image

def create_colored_triangle(width, height, color):
    image = Image.new('RGB', (width, height), 'white')
    pixels = image.load()
    
    for y in range(height):
        for x in range(y + 1):
            pixels[x, y] = color
    
    return image

if __name__ == '__main__':
    triangle_image = create_colored_triangle(10, 10, (255, 0, 0))
    triangle_image.show()