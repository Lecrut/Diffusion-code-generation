def generate_diamond_pattern(center_width):
    if center_width % 2 == 0:
        raise ValueError("Center width must be an odd number.")
    max_stars = center_width
    mid = max_stars // 2
    upper_half = [" " * (mid - i) + "*" * (2 * i + 1) for i in range(mid + 1)]
    lower_half = [" " * (mid - i) + "*" * (2 * i + 1) for i in range(mid - 1, -1, -1)]
    return upper_half + lower_half

if __name__ == '__main__':
    width = 9
    result = generate_diamond_pattern(width)
    for line in result:
        print(line)