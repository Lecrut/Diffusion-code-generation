def print_diamond_pattern(n):
    upper_height = n
    lower_height = n - 1
    for i in range(upper_height):
        spaces = upper_height - 1 - i
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)
    for i in range(lower_height):
        spaces = i + 1
        stars = 2 * (lower_height - i) - 1
        print(" " * spaces + "*" * stars)

if __name__ == '__main__':
    sample_height = 5
    print_diamond_pattern(sample_height)