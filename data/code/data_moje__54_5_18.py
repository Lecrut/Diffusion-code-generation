def hollow_square(size, border_char, interior_char=' '):
    if size < 1:
        return ''
    if size == 1:
        return border_char
    top_bottom = border_char * size
    middle = border_char + interior_char * (size - 2) + border_char
    lines = [top_bottom] + [middle] * (size - 2) + [top_bottom] if size > 2 else [top_bottom]
    return '\n'.join(lines)

if __name__ == '__main__':
    print(hollow_square(5, '*', ' '))
    print(hollow_square(3, '#', '.'))
    print(hollow_square(1, 'X'))
    print(hollow_square(4, '-', '_'))