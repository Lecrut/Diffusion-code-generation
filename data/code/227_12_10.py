def print_diamond_star_pattern():
    n = 7
    upper_half = [('*' * (2*i + 1)).center(n) for i in range(n // 2 + 1)]
    lower_half = upper_half[-2::-1]
    diamond = upper_half + lower_half
    for line in diamond:
        print(line)

if __name__ == '__main__':
    print_diamond_star_pattern()