def generate_checkerboard(width, height):
    checkerboard = []
    pattern = {0: '.', 1: '#'}
    for y in range(height):
        row = ''.join(pattern[(x + y) % 2] for x in range(width))
        checkerboard.append(row)
    return checkerboard

if __name__ == '__main__':
    width, height = 8, 6
    board = generate_checkerboard(width, height)
    for row in board:
        print(row)