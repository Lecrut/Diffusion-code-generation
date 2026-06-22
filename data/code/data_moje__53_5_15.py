def generate_symmetric_reverse_number_triangle(rows=5):
    lines = []
    for i in range(1, rows + 1):
        spaces = ' ' * (i - 1)
        numbers = ' '.join((str(num) for num in range(i, rows + 1)))
        lines.append(spaces + numbers)
    for i in range(rows - 1, 0, -1):
        spaces = ' ' * (i - 1)
        numbers = ' '.join((str(num) for num in range(i, rows + 1)))
        lines.append(spaces + numbers)
    return '\n'.join(lines)
if __name__ == '__main__':
    result = generate_symmetric_reverse_number_triangle(5)
    print(result)