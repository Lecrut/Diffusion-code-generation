def generate_reverse_number_triangle(rows):
    lines = []
    for i in range(rows, 0, -1):
        line = ''.join(str(j) for j in range(1, i + 1))
        lines.append(line)
    for i in range(2, rows + 1):
        line = ''.join(str(j) for j in range(1, i + 1))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_reverse_number_triangle(5)
    print(result)