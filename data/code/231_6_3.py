def generate_staircase(rows, cols):
    pattern = []
    for i in range(rows):
        row_str = ""
        for j in range(cols):
            if (i + j) % 2 == 0:
                row_str += 'A'
            else:
                row_str += 'B'
        pattern.append(row_str)
    return pattern
if __name__ == '__main__':
    rows = 5
    cols = 10
    result = generate_staircase(rows, cols)
    for row in result:
        print(row)