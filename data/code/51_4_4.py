def generate_number_pyramid():
    lines = []
    for row in range(1, 4):
        line = ' ' * (3 - row) + ' '.join(str(i) for i in range(1, row + 1))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_number_pyramid())