if __name__ == '__main__':
    N = 5
    grid = []
    for i in range(N):
        row = "*" * N
        grid.append(row)
    for row in grid:
        print(row)