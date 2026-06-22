def generate_symmetric_reverse_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row_nums = list(range(i, 0, -1))
        row_str = " ".join(str(num) for num in row_nums)
        padding = " " * (rows - i)
        padded_row = padding + row_str + padding
        result.append(padded_row)
    return result

if __name__ == '__main__':
    n = 5
    lines = generate_symmetric_reverse_triangle(n)
    for line in lines:
        print(line)