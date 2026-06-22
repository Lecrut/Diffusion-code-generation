def generate_arrowhead(width):
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer")
    
    arrow = []
    for i in range(1, width + 1):
        row = " " * (width - i) + "*" * (2 * i - 1)
        arrow.append(row)
    return "\n".join(arrow)

if __name__ == '__main__':
    sample_width = 5
    output = generate_arrowhead(sample_width)
    print(output)