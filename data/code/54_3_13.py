def generate_hollow_square(n, border_char='#'):
    if n <= 0:
        return ""
    if n == 1:
        return border_char
    lines = []
    first_line = border_char * n
    lines.append(first_line)
    if n > 2:
        middle_line = border_char + ' ' * (n - 2) + border_char
        for _ in range(n - 2):
            lines.append(middle_line)
    last_line = first_line
    if n > 1:
        lines.append(last_line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_hollow_square(5)
    print(result)
    result_custom = generate_hollow_square(7, '*')
    print(result_custom)