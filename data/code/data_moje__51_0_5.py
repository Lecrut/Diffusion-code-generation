def generate_pyramid(rows=5):
    lines = []
    for i in range(1, rows + 1):
        line = ' ' * (2 * (rows - i)) + ' '.join(str(i) for _ in range(i))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_pyramid(5))