def build_hollow_pyramid(rows: int) -> list:
    if rows <= 0:
        return []
    pyramid = []
    for i in range(1, rows + 1):
        row_str = " " * (rows - i) + "*"
        if i > 1:
            row_str += " " * (2 * i - 3) + "*"
        pyramid.append(row_str)
    return pyramid

if __name__ == '__main__':
    sample_rows = 5
    result = build_hollow_pyramid(sample_rows)
    for line in result:
        print(line)