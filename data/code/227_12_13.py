def print_diamond_star_pattern():
    max_width = 7
    top_half = [('*' * (2 * i + 1)).center(max_width) for i in range((max_width + 1) // 2)]
    bottom_half = top_half[-2::-1]
    diamond = top_half + bottom_half
    for line in diamond:
        print(line)

if __name__ == '__main__':
    print_diamond_star_pattern()