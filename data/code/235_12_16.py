def generate_pyramid_line(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    pattern = []
    for i in range(1, n + 1):
        line = ' '.join(['*'] * (2 * i - 1))
        pattern.append(line.center(n * 3))
    return '\n'.join(pattern)

if __name__ == '__main__':
    sample_number = 5
    result = generate_pyramid_line(sample_number)
    print(result)