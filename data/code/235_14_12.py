def generate_zigzag(width):
    if width <= 0:
        raise ValueError("Width must be greater than 0")
    
    pattern = []
    for i in range(width):
        line = '*' * (2 * i + 1)
        if i % 2 != 0:
            line = line[::-1]
        pattern.append(line)
    
    return '\n'.join(pattern)

if __name__ == '__main__':
    try:
        print(generate_zigzag(5))
    except ValueError as e:
        print(e)