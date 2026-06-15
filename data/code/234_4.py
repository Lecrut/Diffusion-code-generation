def create_checkerboard(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            if (i + j) % 2 == 0:
                row.append(1)
            else:
                row.append(0)
        board.append(row)
    return board
if __name__ == '__main__':
    n_sample = 4
    result = create_checkerboard(n_sample)
    print(result)