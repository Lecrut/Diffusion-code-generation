def print_diamond_star_pattern():
    max_width = 7
    pattern = [
        '*' * (2 * i + 1).center(max_width)
        for i in range((max_width + 1) // 2)
    ] + [
        '*' * (2 * i - 1).center(max_width)
        for i in range((max_width - 1) // 2, -1, -1)
    ]
    print('\n'.join(pattern))

if __name__ == '__main__':
    print_diamond_star_pattern()