def build_hollow_square(size):
    border = '*' * size
    inner = '*' + ' ' * (size - 2) + '*'
    top_and_bottom = border
    middle_lines = []
    for _ in range(size - 2):
        middle_lines.append(inner)
    rows = [top_and_bottom] + middle_lines + [top_and_bottom]
    return '\n'.join(rows)

if __name__ == '__main__':
    result = build_hollow_square(10)
    print(result)