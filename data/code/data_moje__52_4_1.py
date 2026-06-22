def generate_diamond_pattern(center_width=9):
    if center_width % 2 == 0:
        raise ValueError("Center width must be odd for a symmetric diamond")
    half = (center_width - 1) // 2
    lines = []
    for i in range(half + 1):
        stars = 2 * i + 1
        spaces = half - i
        lines.append(' ' * spaces + '*' * stars)
    for i in range(half - 1, -1, -1):
        stars = 2 * i + 1
        spaces = half - i
        lines.append(' ' * spaces + '*' * stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_diamond_pattern(9))