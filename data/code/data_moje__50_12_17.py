def generate_hollow_triangle(size):
    lines = []
    for i in range(size):
        if i == size - 1:
            line = '*' * (2 * i + 1)
        elif i == 0:
            line = '*' * (2 * i + 1)
        else:
            line = '*' + ' ' * (2 * i - 1) + '*'
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_hollow_triangle(5))