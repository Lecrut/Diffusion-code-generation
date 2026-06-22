def print_diamond_star_pattern(max_width):
    if not isinstance(max_width, int) or max_width <= 0:
        raise ValueError("Max width must be a positive integer")
    
    half = (max_width + 1) // 2
    upper_half = [' ' * (half - i - 1) + '*' * (2 * i + 1) for i in range(half)]
    lower_half = upper_half[-2::-1]
    diamond = upper_half + lower_half
    
    for line in diamond:
        print(line)

if __name__ == '__main__':
    try:
        print_diamond_star_pattern(7)
    except ValueError as e:
        print(e)