def generate_diamond_pattern(center_width):
    half = center_width // 2
    lines = []
    lines.extend([" " * (half - i) + "*" * (2 * i + 1) for i in range(half + 1)])
    lines.extend([" " * (half - i) + "*" * (2 * i + 1) for i in range(half - 1, -1, -1)])
    return lines

if __name__ == '__main__':
    result = generate_diamond_pattern(9)
    for line in result:
        print(line)