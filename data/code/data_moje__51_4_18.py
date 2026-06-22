def generate_number_pyramid():
    rows = 3
    lines = []
    for i in range(1, rows + 1):
        line = ' '.join(str(i) for _ in range(i))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_number_pyramid())