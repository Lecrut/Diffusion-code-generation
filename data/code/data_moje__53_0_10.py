def generate_reverse_triangle(rows):
    lines = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        numbers = ' '.join(str(j) for j in range(i, 0, -1))
        lines.append(spaces + numbers)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_reverse_triangle(5)
    print(result)