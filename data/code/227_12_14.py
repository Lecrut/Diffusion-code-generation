def print_diamond_star_pattern():
    max_width = 7
    half_height = (max_width + 1) // 2
    diamond = [
        '*' * (i * 2 - 1).center(max_width)
        for i in range(1, half_height + 1)
    ] + [
        '*' * (i * 2 - 1).center(max_width)
        for i in range(half_height - 1, 0, -1)
    ]
    print('\n'.join(diamond))

if __name__ == '__main__':
    print_diamond_star_pattern()