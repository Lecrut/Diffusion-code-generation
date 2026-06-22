def print_diamond_star_pattern():
    max_width = 7
    upper_half = [('*' * (2*i + 1)).center(max_width) for i in range(max_width // 2 + 1)]
    lower_half = upper_half[-2::-1]
    diamond = upper_half + lower_half
    for line in diamond:
        print(line)

if __name__ == '__main__':
    print_diamond_star_pattern()