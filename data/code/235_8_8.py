def generate_arrowhead_pattern(width):
    if width < 1:
        raise ValueError("Width must be greater than 0")

    pattern = ""
    for i in range(1, width + 2):
        pattern += " " * (width - i) + "*" * (2 * i - 1) + "\n"
    return pattern

if __name__ == '__main__':
    arrowhead = generate_arrowhead_pattern(5)
    print(arrowhead)