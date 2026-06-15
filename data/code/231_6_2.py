import itertools
def generate_snake_pattern(rows, cols):
    pattern = []
    for r in range(rows):
        row_str = ""
        for c in range(cols):
            if (r + c) % 2 == 0:
                row_str += 'A'
            else:
                row_str += 'B'
        pattern.append(row_str)
    return pattern
if __name__ == '__main__':
    rows = 5
    cols = 8
    result = generate_snake_pattern(rows, cols)
    for row in result:
        print(row)