def generate_hollow_square(size, border_char, interior_char):
    if size < 1:
        return ""
    if size == 1:
        return border_char
    
    top_bottom = border_char * size
    middle = border_char + (interior_char * (size - 2)) + border_char
    
    parts = [top_bottom]
    if size > 2:
        parts.extend([middle] * (size - 2))
    if size > 1:
        parts.append(top_bottom)
    
    return '\n'.join(parts)

if __name__ == '__main__':
    result = generate_hollow_square(5, '*', ' ')
    print(result)