def generate_checkerboard(width, height):
    checkerboard = []
    for y in range(height):
        row = []
        for x in range(width):
            if (x + y) % 2 == 0:
                row.append('.')
            else:
                row.append('#')
        checkerboard.append(''.join(row))
    return '\n'.join(checkerboard)

if __name__ == '__main__':
    print(generate_checkerboard(8, 8))