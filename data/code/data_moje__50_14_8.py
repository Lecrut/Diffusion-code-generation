def print_diamond_pattern(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
    for i in range(height - 2, -1, -1):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))

if __name__ == '__main__':
    print_diamond_pattern(5)