def generate_hollow_square(n, border_char='#'):
    if n <= 0:
        return []
    if n == 1:
        return [border_char]
    lines = []
    top_bottom = border_char * n
    middle = border_char + ' ' * (n - 2) + border_char
    lines.append(top_bottom)
    for _ in range(n - 2):
        lines.append(middle)
    lines.append(top_bottom)
    return lines

if __name__ == '__main__':
    result = generate_hollow_square(5)
    for line in result:
        print(line)
    print()
    result_custom = generate_hollow_square(6, border_char='*')
    for line in result_custom:
        print(line)