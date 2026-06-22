def create_checkerboard(N):
    board = []
    for i in range(N):
        row = []
        for j in range(N):
            if (i + j) % 2 == 0:
                row.append('B')
            else:
                row.append('W')
        board.append(row)
    return board

if __name__ == '__main__':
    result8x8 = create_checkerboard(8)
    for row in result8x8:
        print(row)