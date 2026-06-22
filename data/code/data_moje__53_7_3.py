def print_reverse_number_triangle(rows):
    lines = []
    for i in range(rows, 0, -1):
        row_numbers = list(range(i, 0, -1))
        line = ' '.join(str(num) for num in row_numbers)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(print_reverse_number_triangle(6))