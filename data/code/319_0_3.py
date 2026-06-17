if __name__ == '__main__':
    rows = 3
    cols = 4
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    count = 1
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = count
            count += 1
    for row in grid:
        print(row)