def generate_hollow_square(n, char='#'):
    if n <= 0:
        return ""
    if n == 1:
        return char
    rows = []
    top_bottom = (char * n)
    if n == 2:
        rows.append(top_bottom)
        rows.append(top_bottom)
    else:
        middle_part = char + (' ' * (n - 2)) + char
        rows.append(top_bottom)
        for _ in range(n - 2):
            rows.append(middle_part)
        rows.append(top_bottom)
    return '\n'.join(rows)

if __name__ == '__main__':
    print(generate_hollow_square(5, '*'))