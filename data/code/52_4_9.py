def generate_diamond_pattern(center_width):
    half_width = center_width // 2
    top_half = [' ' * (half_width - i) + '*' * (2 * i + 1) for i in range(half_width + 1)]
    bottom_half = [' ' * (half_width - i) + '*' * (2 * i + 1) for i in range(half_width - 1, -1, -1)]
    return top_half + bottom_half

if __name__ == '__main__':
    diamond = generate_diamond_pattern(9)
    for line in diamond:
        print(line)