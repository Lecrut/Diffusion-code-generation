from PIL import Image, ImageDraw

def create_grid_image():
    width, height = 20 * 50, 20 * 50
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    for i in range(1, 20):
        draw.line([(i * 50, 0), (i * 50, height)], fill='black')
        draw.line([(0, i * 50), (width, i * 50)], fill='black')
    
    img.save('grid.png')

if __name__ == '__main__':
    create_grid_image()