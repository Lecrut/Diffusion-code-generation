def generate_checkerboard(width, height):
    checkerboard = [['.' if (x + y) % 2 == 0 else '#' for x in range(width)] for y in range(height)]
    return '\n'.join([''.join(row) for row in checkerboard])

if __name__ == '__main__':
    width, height = 8, 6
    print(generate_checkerboard(width, height))