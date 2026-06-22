def generate_right_aligned_reverse_triangle(rows: int) -> str:
    lines = []
    for i in range(1, rows + 1):
        number = i
        row_str = str(number)
        spaces = ' ' * (rows - i)
        line = spaces + row_str
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    num_rows = 4
    result = generate_right_aligned_reverse_triangle(num_rows)
    print(result)