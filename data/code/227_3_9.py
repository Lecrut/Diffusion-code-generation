def print_diamond_star_pattern(max_width):
    for i in range(1, max_width + 1, 2):
        print(' ' * ((max_width - i) // 2) + '*' * i)
    for i in range(max_width - 2, 0, -2):
        print(' ' * ((max_width - i) // 2) + '*' * i)

if __name__ == '__main__':
    print_diamond_star_pattern(5)