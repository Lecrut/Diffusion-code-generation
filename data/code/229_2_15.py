from PIL import Image

def render_grid(size=256, cell_size=32):
    image = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(image)
    for x in range(0, size, cell_size):
        for y in range(0, size, cell_size):
            draw.rectangle([x, y, x + cell_size, y + cell_size], outline='black')
    image.save('grid.png')

if __name__ == '__main__':
    render_grid()