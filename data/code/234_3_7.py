from PIL import Image

def create_checkerboard(width, height, color1, color2):
    checkerboard = []
    for y in range(height):
        row = []
        for x in range(width):
            if (x + y) % 2 == 0:
                row.append(color1)
            else:
                row.append(color2)
        checkerboard.append(row)

    return checkerboard

def save_checkerboard_image(checkerboard, filename):
    width = len(checkerboard[0])
    height = len(checkerboard)
    image = Image.new('L', (width, height))
    
    for y in range(height):
        for x in range(width):
            image.putpixel((x, y), checkerboard[y][x])

    image.save(filename)

if __name__ == '__main__':
    width_val = 10
    height_val = 8
    color1_val = 255
    color2_val = 0
    filename_val = 'checkerboard.png'
    
    checkerboard = create_checkerboard(width_val, height_val, color1_val, color2_val)
    save_checkerboard_image(checkerboard, filename_val)
    print(f'Checkerboard image saved as {filename_val}')