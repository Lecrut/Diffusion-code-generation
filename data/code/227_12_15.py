def print_diamond_star_pattern(max_width):
    if max_width % 2 == 0:
        raise ValueError("Max width must be an odd number")
    
    half = (max_width + 1) // 2
    diamond = [
        ' ' * (half - i - 1) + '*' * (2 * i + 1)
        for i in range(half)
    ] + [
        ' ' * (half - i - 1) + '*' * (2 * i + 1)
        for i in range(half - 2, -1, -1)
    ]
    
    for line in diamond:
        print(line)

if __name__ == '__main__':
    try:
        print_diamond_star_pattern(7)
    except ValueError as e:
        print(e)