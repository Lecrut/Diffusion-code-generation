def print_right_aligned_triangle():
    row_count = 10
    lines = []
    for i in range(1, row_count + 1):
        line = ' ' * (row_count - i) + '*' * i
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    result = print_right_aligned_triangle()
    print(result)