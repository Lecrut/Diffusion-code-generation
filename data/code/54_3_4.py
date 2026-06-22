def generate_hollow_square(n, char='#'):
    if n <= 0:
        return ''
    if n == 1:
        return char
    
    lines = []
    border = char * n
    inner = char + (n - 2) * ' ' + char
    
    lines.append(border)
    for _ in range(n - 2):
        lines.append(inner)
    if n > 1:
        lines.append(border)
    
    return '\n'.join(lines)

if __name__ == '__main__':
    n = 5
    char = '*'
    result = generate_hollow_square(n, char)
    print(result)