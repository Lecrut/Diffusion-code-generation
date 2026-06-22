from PIL import Image

def create_checkerboard(width, height, cell_size, color1, color2):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")
    if cell_size <= 0:
        raise ValueError("Cell size must be a positive integer.")
    if len(color1) != 3 or len(color2) != 3:
        raise ValueError("Color values must be tuples of three integers.")

    image = Image.new('RGB', (width * cell_size, height * cell_size))
    pixels = image.load()

    for r in range(height):
        for c in range(width):
            if (r + c) % 2 == 0:
                pixels[c * cell_size:(c + 1) * cell_size, r * cell_size:(r + 1) * cell_size] = color1
            else:
                pixels[c * cell_size:(c + 1) * cell_size, r * cell_size:(r + 1) * cell_size] = color2

    return image

if __name__ == '__main__':
    width_val = 8
    height_val = 6
    cell_size_val = 50
    color1_val = (255, 0, 0)
    color2_val = (0, 0, 255)

    checkerboard_image = create_checkerboard(width_val, height_val, cell_size_val, color1_val, color2_val)
    checkerboard_image.save('checkerboard.png')