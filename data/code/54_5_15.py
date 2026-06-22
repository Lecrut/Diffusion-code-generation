def generate_hollow_square(size, border_char='*', interior_spacing=' '):
    if size <= 0:
        return ""
    if size == 1:
        return border_char
    
    top_bottom = border_char * size
    middle = border_char + interior_spacing * (size - 2) + border_char
    
    middle_rows = [middle] * (size - 2)
    
    if size == 2:
        return top_bottom + '\n' + top_bottom
    
    return '\n'.join([top_bottom] + middle_rows + [top_bottom])

if __name__ == '__main__':
    result = generate_hollow_square(5, '*', ' ')
    print(result)