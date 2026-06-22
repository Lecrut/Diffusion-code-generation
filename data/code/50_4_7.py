def render_hollow_triangle(size=8):
    lines = []
    for i in range(1, size + 1):
        if i == 1:
            line = ' ' * (size - i) + '*'
        elif i == size:
            line = '*' * (2 * i - 1)
        else:
            line = ' ' * (size - i) + '*' + ' ' * (2 * i - 3) + '*'
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(render_hollow_triangle(8))