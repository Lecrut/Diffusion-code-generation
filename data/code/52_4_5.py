def generate_diamond_pattern(center_width):
    if center_width % 2 == 0 or center_width < 1:
        raise ValueError("Center width must be an odd positive integer.")
    half_height = center_width // 2
    upper_half = [" " * (half_height - i) + "*" * (2 * i + 1) for i in range(half_height + 1)]
    lower_half = [" " * (half_height - i) + "*" * (2 * i + 1) for i in range(half_height - 1, -1, -1)]
    return upper_half + lower_half

if __name__ == '__main__':
    result = generate_diamond_pattern(9)
    for line in result:
        print(line)