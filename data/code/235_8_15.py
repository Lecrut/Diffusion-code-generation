def generate_arrowhead_pattern(width):
    if width < 1:
        raise ValueError("Width must be at least 1")
    
    pattern = ""
    for i in range(1, width + 1):
        pattern += " " * (width - i) + "*" * (2 * i - 1) + "\n"
    return pattern

if __name__ == '__main__':
    arrowhead_width = 5
    output = generate_arrowhead_pattern(arrowhead_width)
    print(output.rstrip())