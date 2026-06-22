def print_reverse_number_triangle(rows=6):
    lines = []
    for i in range(rows, 0, -1):
        row = [str(j) for j in range(1, i + 1)]
        lines.append(' '.join(row))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(print_reverse_number_triangle())