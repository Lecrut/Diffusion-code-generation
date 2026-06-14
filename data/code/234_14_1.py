def generate_checkerboard(rows, cols, char1='X', char2='O'):
    grid = []
    for r in range(rows):
        row_data = []
        for c in range(cols):
            if (r + c) % 2 == 0:
                row_data.append(char1)
            else:
                row_data.append(char2)
        grid.append(" ".join(row_data))
    return "\n".join(grid)
if __name__ == '__main__':
    rows = 5
    cols = 7
    result = generate_checkerboard(rows, cols)
    print(result)