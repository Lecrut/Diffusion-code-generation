def generate_hollow_square(n, border_char='#'):
    if n <= 0:
        return []
    if n == 1:
        return [border_char]
    if n == 2:
        return [border_char * 2, border_char * 2]
    
    first_row = border_char * n
    middle_row = border_char + ' ' * (n - 2) + border_char
    last_row = border_char * n
    
    result = [first_row]
    for _ in range(n - 2):
        result.append(middle_row)
    result.append(last_row)
    return result

if __name__ == '__main__':
    sample_size = 5
    sample_char = '#'
    output = generate_hollow_square(sample_size, sample_char)
    for line in output:
        print(line)
    print()
    output_2 = generate_hollow_square(3, '*')
    for line in output_2:
        print(line)