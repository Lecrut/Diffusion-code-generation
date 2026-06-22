from PIL import Image, ImageDraw

def create_grid_image():
    size = 20
    cell_size = 20
    border_color = (0, 0, 0)
    fill_color = (255, 255, 255)

    img = Image.new('RGB', (size * cell_size, size * cell_size), fill=fill_color)
    draw = ImageDraw.Draw(img)

    for i in range(size + 1):
        draw.line([(i * cell_size, 0), (i * cell_size, size * cell_size)], fill=border_color)
        draw.line([(0, i * cell_size), (size * cell_size, i * cell_size)], fill=border_color)

    return img

if __name__ == '__main__':
    grid_image = create_grid_image()
    grid_image.save('grid.png')