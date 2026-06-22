from PIL import Image

def create_grid_image():
    width, height = 20, 20
    cell_size = 30
    img_width = width * cell_size
    img_height = height * cell_size
    image = Image.new('RGB', (img_width, img_height), 'white')
    
    for x in range(width):
        for y in range(height):
            left = x * cell_size
            top = y * cell_size
            right = left + cell_size
            bottom = top + cell_size
            image.paste((0, 0, 0), (left, top, right, bottom))
    
    return image

if __name__ == '__main__':
    grid_image = create_grid_image()
    grid_image.save('grid.png')