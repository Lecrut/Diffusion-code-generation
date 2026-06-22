def generate_hollow_square(size: int, border_char: str = '*', interior_char: str = ' ') -> str:
    top_bottom_row = (border_char * size) if size > 0 else ''
    middle_row = (border_char + (interior_char * (size - 2)) + border_char) if size > 1 else top_bottom_row
    
    if size == 0:
        return ''
    if size == 1:
        return top_bottom_row
    if size == 2:
        return '\n'.join([top_bottom_row, top_bottom_row])
    
    middle_rows = '\n'.join([middle_row] * (size - 2))
    return f"{top_bottom_row}\n{middle_rows}\n{top_bottom_row}"

if __name__ == '__main__':
    result = generate_hollow_square(5, '#', ' ')
    print(result)