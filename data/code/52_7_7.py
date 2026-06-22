def construct_diamond_pattern(size):
    lines = []
    for i in range(1, size + 1):
        lines.append(' ' * (size - i) + '*' * (2 * i - 1))
    for i in range(size - 1, 0, -1):
        lines.append(' ' * (size - i) + '*' * (2 * i - 1))
    return lines

def display_diamond_pattern(pattern_lines):
    for line in pattern_lines:
        print(line)

if __name__ == '__main__':
    size = 5
    diamond = construct_diamond_pattern(size)
    display_diamond_pattern(diamond)