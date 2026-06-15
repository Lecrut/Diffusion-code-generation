def create_checkerboard(size):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            if (i + j) % 2 == 0:
                row.append(1)
            else:
                row.append(0)
        board.append(row)
    return board
if __name__ == '__main__':
    size = 4
    checkerboard = create_checkerboard(size)
    for row in checkerboard:
        print(row)