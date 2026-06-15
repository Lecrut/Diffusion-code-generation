def generate_checkerboard(rows, cols):
    board = []
    for r in range(rows):
        row_list = []
        for c in range(cols):
            if (r + c) % 2 == 0:
                row_list.append(' ' if r % 2 == 0 else 'X')
            else:
                row_list.append('X' if r % 2 == 0 else ' ')
        board.append(row_list)
    return board
def generate_checkerboard_pythonic(rows, cols):
    board = []
    for r in range(rows):
        row = [('X' if (r + c) % 2 == 0 else ' ') for c in range(cols)]
        board.append(row)
    return board
if __name__ == '__main__':
    R = 5
    C = 8
    checkerboard = generate_checkerboard_pythonic(R, C)
    for row in checkerboard:
        print("".join(row))