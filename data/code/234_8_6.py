def generate_checkerboard(rows, cols):
    board = []
    for r in range(rows):
        row_str = []
        for c in range(cols):
            if (r + c) % 2 == 0:
                row_str.append(' ' if r % 2 == 0 else 'X')
            else:
                row_str.append('X' if r % 2 == 0 else ' ')
        board.append("".join(row_str))
    return board
def generate_checkerboard_pythonic(rows, cols):
    board = []
    for r in range(rows):
        row = []
        for c in range(cols):
            if (r + c) % 2 == 0:
                row.append('X')
            else:
                row.append(' ')
        board.append("".join(row))
    return board
def generate_checkerboard_list_comprehension(rows, cols):
    board = []
    for r in range(rows):
        row_chars = [('X' if (r + c) % 2 == 0 else ' ') for c in range(cols)]
        board.append("".join(row_chars))
    return board
if __name__ == '__main__':
    R = 5
    C = 8
    checkerboard = generate_checkerboard_list_comprehension(R, C)
    for row in checkerboard:
        print(row)