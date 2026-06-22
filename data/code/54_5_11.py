def generate_hollow_square(size, border_char='*', interior_char=' '):
    if size < 1:
        return ""
    if size == 1:
        return border_char
    
    top_bottom = border_char * size
    middle = border_char + interior_char * (size - 2) + border_char
    
    rows = [top_bottom] + [middle] * (size - 2) + [top_bottom]
    
    return '\n'.join(rows)

if __name__ == '__main__':
    result = generate_hollow_square(5, '#', '.')
    print(result)