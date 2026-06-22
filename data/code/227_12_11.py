def print_diamond_star_pattern(max_width):
    half = max_width // 2 + 1
    upper_half = [' ' * (half - i - 1) + '*' * (2 * i + 1) for i in range(half)]
    lower_half = upper_half[-2::-1]
    diamond = upper_half + lower_half
    for line in diamond:
        print(line)

if __name__ == '__main__':
    print_diamond_star_pattern(7)