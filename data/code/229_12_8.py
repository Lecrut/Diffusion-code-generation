from PIL import Image, ImageDraw

def create_grid_image():
    size = 20
    cell_size = 20
    border_width = 1
    
    image = Image.new('RGB', (size * cell_size, size * cell_size), 'white')
    draw = ImageDraw.Draw(image)
    
    for i in range(size + 1):
        x1, y1 = i * cell_size, 0
        x2, y2 = i * cell_size, size * cell_size
        draw.line((x1, y1, x2, y2), fill='black', width=border_width)
        
        x1, y1 = 0, i * cell_size
        x2, y2 = size * cell_size, i * cell_size
        draw.line((x1, y1, x2, y2), fill='black', width=border_width)
    
    return image

if __name__ == '__main__':
    grid_image = create_grid_image()
    grid_image.save('grid.png')