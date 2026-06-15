def generate_checkerboard(rows, cols):
    board = []
    for r in range(rows):
        row_str = ""
        for c in range(cols):
            if (r + c) % 2 == 0:
                row_str += " "
            else:
                row_str += "#"
        board.append(row_str)
    return board
def generate_checkerboard_pythonic(rows, cols):
    board = []
    for r in range(rows):
        row = [" " if (r + c) % 2 == 0 else "#" for c in range(cols)]
        board.append("".join(row))
    return board
if __name__ == '__main__':
    R = 5
    C = 8
    checkerboard = generate_checkerboard_pythonic(R, C)
    for row in checkerboard:
        print(row)