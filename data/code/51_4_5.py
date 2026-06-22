def generate_number_pyramid():
    rows = 3
    lines = []
    for row_num in range(1, rows + 1):
        spaces = ' ' * (rows - row_num)
        numbers = ' '.join(str(n) for n in range(1, row_num + 1))
        lines.append(spaces + numbers)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_number_pyramid())