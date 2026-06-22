def generate_diamond_pattern():
    center_width = 9
    half = (center_width - 1) // 2
    lines = []
    for i in range(-half, half + 1):
        stars = 2 * (half - abs(i)) + 1
        spaces = abs(i)
        lines.append(' ' * spaces + '*' * stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_diamond_pattern())