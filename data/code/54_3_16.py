def generate_hollow_square(n, char='#'):
    if n <= 0:
        return ''
    if n == 1:
        return char
    lines = []
    top_bottom = char * n
    middle = char + ' ' * (n - 2) + char
    lines.append(top_bottom)
    for _ in range(n - 2):
        lines.append(middle)
    lines.append(top_bottom)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_hollow_square(5))
    print(generate_hollow_square(3, '*'))
    print(generate_hollow_square(1, 'X'))
    print(generate_hollow_square(10))