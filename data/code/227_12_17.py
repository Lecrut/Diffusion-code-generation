def print_diamond_star_pattern():
    width = 7
    half_width = (width + 1) // 2
    pattern = [
        '*' * (i * 2 - 1).center(width)
        for i in range(1, half_width + 1)
    ] + [
        '*' * (i * 2 - 1).center(width)
        for i in range(half_width - 1, 0, -1)
    ]
    print('\n'.join(pattern))

if __name__ == '__main__':
    print_diamond_star_pattern()