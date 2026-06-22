from PIL import Image

def create_colored_triangle(width, height, color):
    img = Image.new('RGB', (width, height), 'white')
    pixels = img.load()
    
    for x in range(width):
        for y in range(height):
            if x + y < width:
                pixels[x, y] = color
    
    return img

if __name__ == '__main__':
    triangle_image = create_colored_triangle(200, 200, (255, 0, 0))
    triangle_image.show()