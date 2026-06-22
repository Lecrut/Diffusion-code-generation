def print_inverted_pyramid(base_width):
    for i in range(base_width, 0, -1):
        print(' ' * (base_width - i) + '*' * (2 * i - 1))

if __name__ == '__main__':
    print("--- Inverted Pyramid with Base Width 9 ---")
    print_inverted_pyramid(9)