def generate_checkerboard(width, height):
    checkerboard = []
    char_map = {'even': '.', 'odd': '#'}
    for y in range(height):
        row = ''.join(char_map[(x + y) % 2 == 0] for x in range(width))
        checkerboard.append(row)
    return checkerboard

if __name__ == '__main__':
    width, height = 8, 6
    board = generate_checkerboard(width, height)
    for row in board:
        print(row)