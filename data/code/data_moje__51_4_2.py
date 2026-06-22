def generate_number_pyramid(rows=3):
    lines = []
    for i in range(1, rows + 1):
        line = ' ' * (rows - i) + ' '.join(str(j) for j in range(1, 2 * i))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_number_pyramid())