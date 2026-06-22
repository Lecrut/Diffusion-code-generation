from PIL import Image

def create_grid_image():
    width = 20 * 50
    height = 20 * 50
    image = Image.new('RGB', (width, height), 'white')
    for i in range(1, 20):
        image.putpixel((i * 50 - 1, 0), 'black')
        image.putpixel((i * 50 - 1, height - 1), 'black')
        image.putpixel((0, i * 50 - 1), 'black')
        image.putpixel((width - 1, i * 50 - 1), 'black')
    image.save('grid.png')
if __name__ == '__main__':
    create_grid_image()