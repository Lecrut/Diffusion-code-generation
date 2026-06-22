def generate_hollow_square(n, border_char='#'):
    if n <= 0:
        return []
    if n == 1:
        return [border_char]
    
    rows = []
    first_last_row = border_char * n
    middle_row = border_char + ' ' * (n - 2) + border_char
    
    rows.append(first_last_row)
    for _ in range(n - 2):
        rows.append(middle_row)
    rows.append(first_last_row)
    
    return rows

if __name__ == '__main__':
    result = generate_hollow_square(5)
    for line in result:
        print(line)
    print()
    result2 = generate_hollow_square(7, '*')
    for line in result2:
        print(line)