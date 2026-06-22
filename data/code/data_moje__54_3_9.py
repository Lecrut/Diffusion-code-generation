def generate_hollow_square(n, border_char='#'):
    if n <= 0:
        return []
    if n == 1:
        return [border_char]
    lines = []
    first_last_line = border_char * n
    middle_line = border_char + ' ' * (n - 2) + border_char
    lines.append(first_last_line)
    for _ in range(n - 2):
        lines.append(middle_line)
    lines.append(first_last_line)
    return lines

if __name__ == '__main__':
    result = generate_hollow_square(5, '*')
    for line in result:
        print(line)
    print()
    result_default = generate_hollow_square(4)
    for line in result_default:
        print(line)
    print()
    result_single = generate_hollow_square(1, 'X')
    for line in result_single:
        print(line)
    print()
    result_zero = generate_hollow_square(0)
    print(result_zero)