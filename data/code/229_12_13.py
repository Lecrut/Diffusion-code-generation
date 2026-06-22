from PIL import Image, ImageDraw

def create_grid_image():
    size = 20
    cell_size = 30
    image = Image.new('RGB', (size * cell_size, size * cell_size), 'white')
    draw = ImageDraw.Draw(image)
    
    for i in range(size + 1):
        draw.line([(i * cell_size, 0), (i * cell_size, size * cell_size)], fill='black')
        draw.line([(0, i * cell_size), (size * cell_size, i * cell_size)], fill='black')
    
    image.save('grid.png')

if __name__ == '__main__':
    create_grid_image()