def generate_diamond_pattern(center_width=9):
    if center_width % 2 == 0:
        raise ValueError("Center width must be odd")
    half = (center_width - 1) // 2
    top_rows = [' ' * (half - i) + '*' * (2 * i + 1) for i in range(half + 1)]
    bottom_rows = [' ' * (i + 1) + '*' * (center_width - 2 * (i + 1)) for i in range(half)]
    return '\n'.join(top_rows + bottom_rows)

if __name__ == '__main__':
    print(generate_diamond_pattern(9))