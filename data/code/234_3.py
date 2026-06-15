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
    rows = 4
    cols = 5
    checkerboard_pattern = generate_checkerboard(rows, cols)
    print(checkerboard_pattern)