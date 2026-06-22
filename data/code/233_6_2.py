def generate_checkerboard(width, height):
    checkerboard = []
    for y in range(height):
        row = ''.join(['#' if (x + y) % 2 else '.' for x in range(width)])
        checkerboard.append(row)
    return checkerboard

if __name__ == '__main__':
    width = 8
    height = 6
    result = generate_checkerboard(width, height)
    for row in result:
        print(row)