def generate_arrowhead(width):
    if width < 1:
        raise ValueError("Width must be at least 1")
    
    arrowhead = []
    for i in range(width):
        row = " " * (width - i - 1) + "*" * (2 * i + 1)
        arrowhead.append(row)
    
    return "\n".join(arrowhead)

if __name__ == '__main__':
    arrow = generate_arrowhead(5)
    print(arrow)