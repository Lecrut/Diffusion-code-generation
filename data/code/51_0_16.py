def generate_pyramid(rows=5):
    lines = []
    for i in range(1, rows + 1):
        line = str(i) * i
        lines.append(line.rjust(rows * 2))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_pyramid())