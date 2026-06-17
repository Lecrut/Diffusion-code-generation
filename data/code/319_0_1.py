if __name__ == '__main__':
    rows = 3
    cols = 4
    grid = []
    count = 1
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(count)
            count += 1
        grid.append(row)
    for row in grid:
        print(*row)