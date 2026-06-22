def print_diamond():
    height = 7
    mid = height // 2
    for i in range(height):
        spaces = abs(mid - i)
        stars = height - 2 * spaces
        print(" " * spaces + "*" * stars)

if __name__ == '__main__':
    print_diamond()