def generate_hollow_square(size, border_char='*', interior_char=' '):
    if size < 1:
        return ""
    if size == 1:
        return border_char
    top_bottom = border_char * size
    middle_row = border_char + interior_char * (size - 2) + border_char
    rows = [top_bottom] + [middle_row] * (size - 2) + [top_bottom]
    return "\n".join(rows)

if __name__ == '__main__':
    print(generate_hollow_square(5, '#', '-'))
    print(generate_hollow_square(1, 'X', ' '))
    print(generate_hollow_square(3, '@', 'o'))