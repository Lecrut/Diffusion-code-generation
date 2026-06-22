def print_right_aligned_triangle(row_count: int = 10) -> str:
    result_lines = []
    for i in range(1, row_count + 1):
        line = '*' * i
        result_lines.append(line.rjust(row_count))
    return '\n'.join(result_lines)

if __name__ == '__main__':
    print(print_right_aligned_triangle())