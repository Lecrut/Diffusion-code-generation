def print_reverse_number_triangle(rows=4):
    lines = []
    for i in range(rows, 0, -1):
        row_str = ''.join(str(j) for j in range(1, i + 1))
        lines.append(row_str.rjust(rows))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(print_reverse_number_triangle())