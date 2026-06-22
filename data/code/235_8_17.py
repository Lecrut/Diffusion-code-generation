def generate_arrowhead_pattern(width):
    if width < 3:
        raise ValueError("Width must be at least 3")
    
    pattern = []
    for i in range(1, width + 1):
        pattern.append(' ' * (width - i) + '*' * i)
    return '\n'.join(pattern)

if __name__ == '__main__':
    arrowhead_width = 5
    print(generate_arrowhead_pattern(arrowhead_width))