def generate_hollow_square(n, border_char='#'):
    if n <= 0:
        return ""
    if n == 1:
        return border_char
    result = []
    result.append(border_char * n)
    inner_space = n - 2
    inner_line = border_char + ' ' * inner_space + border_char
    for _ in range(n - 2):
        result.append(inner_line)
    result.append(border_char * n)
    return '\n'.join(result)

if __name__ == '__main__':
    sample_n = 5
    sample_char = '*'
    print(generate_hollow_square(sample_n, sample_char))
    print(generate_hollow_square(1, '@'))
    print(generate_hollow_square(4))