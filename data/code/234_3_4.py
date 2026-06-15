def generate_checkerboard(rows, cols):
    board = []
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                board.append(0)
            else:
                board.append(1)
    return board
if __name__ == '__main__':
    rows = 4
    cols = 5
    checkerboard_pattern = generate_checkerboard(rows, cols)
    print(checkerboard_pattern)