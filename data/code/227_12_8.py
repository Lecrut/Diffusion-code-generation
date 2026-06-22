def print_diamond_star_pattern():
    n = 3
    upper_half = [('*' * (2*i + 1)).center(7) for i in range(n)]
    lower_half = upper_half[-2::-1]
    diamond = upper_half + lower_half
    for line in diamond:
        print(line)

if __name__ == '__main__':
    print_diamond_star_pattern()