def create_checkerboard(N):
    checkerboard = [[(i + j) % 2 for j in range(N)] for i in range(N)]
    return checkerboard

if __name__ == '__main__':
    N = 8
    board = create_checkerboard(N)
    for row in board:
        print(row)