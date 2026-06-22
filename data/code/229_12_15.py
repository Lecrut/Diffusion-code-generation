from PIL import Image, ImageDraw

def create_grid_image():
    size = 20
    cell_size = 20
    border_width = 1
    interior_color = (255, 255, 255)
    border_color = (0, 0, 0)

    img = Image.new('RGB', (size * cell_size, size * cell_size), border_color)
    draw = ImageDraw.Draw(img)

    for i in range(size):
        for j in range(size):
            x1 = i * cell_size + border_width
            y1 = j * cell_size + border_width
            x2 = (i + 1) * cell_size - border_width
            y2 = (j + 1) * cell_size - border_width
            draw.rectangle([x1, y1, x2, y2], outline=border_color, fill=interior_color)

    return img

if __name__ == '__main__':
    grid_img = create_grid_image()
    grid_img.save('grid.png')