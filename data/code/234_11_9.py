def create_checkerboard(N):
    checkerboard = []
    for i in range(N):
        row = []
        for j in range(N):
            if (i + j) % 2 == 0:
                cell_value = 'B'
            else:
                cell_value = 'W'
            row.append(cell_value)
        checkerboard.append(row)
    return checkerboard

if __name__ == '__main__':
    N1 = 6
    board1 = create_checkerboard(N1)
    for row in board1:
        print(row)

    N2 = 5
    board2 = create_checkerboard(N2)
    for row in board2:
        print(row)