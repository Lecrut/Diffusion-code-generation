def print_diamond_pattern(half_height):
    for i in range(half_height):
        spaces = half_height - 1 - i
        stars = 2 * i + 1
        print(' ' * spaces + '*' * stars)
    for i in range(half_height - 1, -1, -1):
        spaces = half_height - 1 - i
        stars = 2 * i + 1
        print(' ' * spaces + '*' * stars)

if __name__ == '__main__':
    sample_height = 4
    print_diamond_pattern(sample_height)