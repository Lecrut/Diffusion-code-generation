def generate_downward_triangle(row_count):
    lines = []
    for i in range(row_count, 0, -1):
        line = ' ' * (row_count - i) + '* ' * i
        lines.append(line.rstrip())
    return '\n'.join(lines)

if __name__ == '__main__':
    rows = 9
    result = generate_downward_triangle(rows)
    print(result)