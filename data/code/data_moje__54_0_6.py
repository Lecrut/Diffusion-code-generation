def generate_hollow_square(n):
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    
    lines = []
    
    for i in range(n):
        if i == 0 or i == n - 1:
            line = '*' * n
        else:
            line = '*' + ' ' * (n - 2) + '*'
        lines.append(line)
    
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_hollow_square(5)
    print(result)