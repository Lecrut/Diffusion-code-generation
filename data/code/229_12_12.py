from PIL import Image, ImageDraw

def create_grid_image():
    size = 20
    cell_size = 20
    border_color = (0, 0, 0)
    interior_color = (255, 255, 255)

    img = Image.new('RGB', (size * cell_size, size * cell_size), border_color)
    draw = ImageDraw.Draw(img)

    for i in range(size):
        for j in range(size):
            x1 = i * cell_size
            y1 = j * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            draw.rectangle([x1, y1, x2, y2], fill=interior_color)

    img.save('grid.png')

if __name__ == '__main__':
    create_grid_image()