def print_diamond_pattern(size):
    half_size = size // 2
    for i in range(half_size + 1):
        spaces = ' ' * (half_size - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    for i in range(half_size - 1, -1, -1):
        spaces = ' ' * (half_size - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

if __name__ == '__main__':
    sample_size = 5
    print_diamond_pattern(sample_size)