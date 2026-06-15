def generate_checkerboard(rows, cols):
    pattern = []
    for r in range(rows):
        for c in range(cols):
            if (r + c) % 2 == 0:
                pattern.append(0)
            else:
                pattern.append(1)
    return pattern
if __name__ == '__main__':
    rows_val = 4
    cols_val = 5
    checkerboard_list = generate_checkerboard(rows_val, cols_val)
    print(checkerboard_list)