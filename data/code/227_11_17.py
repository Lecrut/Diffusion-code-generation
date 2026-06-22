def generate_star_pattern(n):
    if n <= 0:
        raise ValueError("Height must be greater than zero")
    
    pattern = []
    for i in range(n):
        row = [' ' * i + '*' + ' ' * (n - i - 1)] * 2
        pattern.append('\n'.join(row))
    
    return '\n'.join(pattern)

if __name__ == '__main__':
    print(generate_star_pattern(4))