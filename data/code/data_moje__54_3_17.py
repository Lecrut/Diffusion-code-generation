def generate_hollow_square(n, border_char='#'):
    if n <= 0:
        return []
    if n == 1:
        return [border_char]
    
    result = []
    full_line = border_char * n
    middle_line = border_char + ' ' * (n - 2) + border_char
    
    result.append(full_line)
    for _ in range(n - 2):
        result.append(middle_line)
    result.append(full_line)
    
    return result

if __name__ == '__main__':
    sample_size = 7
    sample_char = '@'
    square_pattern = generate_hollow_square(sample_size, sample_char)
    for line in square_pattern:
        print(line)