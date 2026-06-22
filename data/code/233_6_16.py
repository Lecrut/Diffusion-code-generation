def generate_checkerboard(width, height):
    checkerboard = []
    for y in range(height):
        row = ''.join(['#' if (x + y) % 2 else '.' for x in range(width)])
        checkerboard.append(row)
    return '\n'.join(checkerboard)

if __name__ == '__main__':
    print(generate_checkerboard(8, 8))