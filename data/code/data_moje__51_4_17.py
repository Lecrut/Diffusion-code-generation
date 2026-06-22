def generate_number_pyramid():
    rows = 3
    lines = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        lines.append(spaces + numbers)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_number_pyramid())