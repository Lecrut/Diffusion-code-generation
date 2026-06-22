def print_diamond_star_pattern(max_width):
    pattern = [' ' * (max_width - i) + '*' * (2 * i - 1) for i in range(1, max_width + 1)]
    pattern += pattern[-2::-1]
    for line in pattern:
        print(line)

if __name__ == '__main__':
    print_diamond_star_pattern(7)