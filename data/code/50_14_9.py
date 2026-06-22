def print_diamond_pattern(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))
    for i in range(height - 1, 0, -1):
        print(" " * (height - i) + "*" * (2 * i - 1))

if __name__ == '__main__':
    sample_height = 5
    print_diamond_pattern(sample_height)