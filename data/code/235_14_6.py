def generate_zigzag_line(width):
    if width < 1:
        raise ValueError("Width must be at least 1")
    
    pattern = []
    for i in range(width):
        line = [' ' * (width - i - 1) + '*' * (2 * i + 1)]
        if i % 2 == 0:
            pattern.extend(line)
        else:
            pattern.extend(reversed(line))
    return '\n'.join(pattern)

if __name__ == '__main__':
    print(generate_zigzag_line(5))