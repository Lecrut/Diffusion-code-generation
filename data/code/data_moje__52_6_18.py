def print_diamond_pattern(size):
    total_lines = 2 * size - 1
    mid = size - 1
    for i in range(total_lines):
        spaces = abs(mid - i)
        stars = size - spaces
        print(' ' * spaces + '*' * (2 * stars - 1))

if __name__ == '__main__':
    print_diamond_pattern(8)