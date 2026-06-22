from PIL import Image, ImageDraw

def create_grid_image(size=20):
    cell_size = 20
    image = Image.new('RGB', (size * cell_size, size * cell_size), 'white')
    draw = ImageDraw.Draw(image)
    for i in range(1, size + 1):
        draw.line([(i * cell_size, 0), (i * cell_size, size * cell_size)], fill='black')
        draw.line([(0, i * cell_size), (size * cell_size, i * cell_size)], fill='black')
    return image

if __name__ == '__main__':
    grid_image = create_grid_image()
    grid_image.save('grid.png')