def generate_hollow_square(size, border_char, interior_char):
    if size <= 0:
        return ""
    if size == 1:
        return border_char
    
    top_bottom = border_char * size
    middle = border_char + (interior_char * (size - 2)) + border_char
    
    rows = [top_bottom]
    if size > 2:
        rows.extend([middle] * (size - 2))
    if size > 1:
        rows.append(top_bottom)
    
    return '\n'.join(rows)

if __name__ == '__main__':
    result = generate_hollow_square(5, '*', ' ')
    print(result)