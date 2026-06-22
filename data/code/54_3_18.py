def generate_hollow_square(size, border_char='#'):
    if size <= 0:
        return []
    if size == 1:
        return [border_char]
    
    result = []
    first_row = border_char * size
    middle_row = border_char + ' ' * (size - 2) + border_char
    
    result.append(first_row)
    for _ in range(size - 2):
        result.append(middle_row)
    result.append(first_row)
    
    return result

if __name__ == '__main__':
    sample_n = 5
    sample_char = '*'
    square_lines = generate_hollow_square(sample_n, sample_char)
    for line in square_lines:
        print(line)