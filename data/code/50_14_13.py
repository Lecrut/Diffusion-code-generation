def print_diamond_pattern(size: int) -> None:
    upper_half_limit = size - 1
    for i in range(size):
        spaces = upper_half_limit - i
        stars = 2 * i + 1
        print(' ' * spaces + '*' * stars)
    
    for i in range(size - 2, -1, -1):
        spaces = upper_half_limit - i
        stars = 2 * i + 1
        print(' ' * spaces + '*' * stars)

if __name__ == '__main__':
    sample_size = 5
    print_diamond_pattern(sample_size)