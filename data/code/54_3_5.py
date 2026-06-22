def generate_hollow_square(n, char='#'):
    if n < 1:
        return []
    if n == 1:
        return [char]
    
    lines = []
    top_bottom = char * n
    middle = char + (n - 2) * ' ' + char
    
    lines.append(top_bottom)
    for _ in range(n - 2):
        lines.append(middle)
    if n > 1:
        lines.append(top_bottom)
    
    return lines

if __name__ == '__main__':
    result1 = generate_hollow_square(5)
    for line in result1:
        print(line)
    print()
    
    result2 = generate_hollow_square(7, '*')
    for line in result2:
        print(line)
    print()
    
    result3 = generate_hollow_square(1, 'X')
    for line in result3:
        print(line)