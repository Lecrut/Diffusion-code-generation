def generate_checkerboard(width, height):
    checkerboard = []
    for y in range(height):
        row = ''
        for x in range(width):
            if (x + y) % 2 == 0:
                row += '.'
            else:
                row += '#'
        checkerboard.append(row)
    return checkerboard

if __name__ == '__main__':
    width, height = 8, 8
    board = generate_checkerboard(width, height)
    for row in board:
        print(row)