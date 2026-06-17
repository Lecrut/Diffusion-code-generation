def generate_grid(rows, cols):
    grid = []
    count = 1
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(str(count))
            count += 1
        grid.append(" ".join(row))
    return grid
if __name__ == '__main__':
    rows = 3
    cols = 4
    result = generate_grid(rows, cols)
    for row_str in result:
        print(row_str)