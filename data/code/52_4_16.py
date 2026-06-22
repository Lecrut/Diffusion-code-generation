def generate_diamond_star_pattern(fixed_width=9):
    if fixed_width % 2 == 0:
        raise ValueError("Fixed width must be an odd number for a centered diamond.")
    half_width = fixed_width // 2 + 1
    upper_half = [('*' * (2 * i + 1)).center(fixed_width) for i in range(half_width)]
    lower_half = [upper_half[i] for i in range(half_width - 2, -1, -1)]
    return upper_half + lower_half

if __name__ == '__main__':
    pattern = generate_diamond_star_pattern(9)
    for line in pattern:
        print(line)