def print_inverted_pyramid(base_width):
    for i in range(base_width // 2 + 1):
        spaces = ' ' * i
        stars = '*' * (base_width - 2 * i)
        print(spaces + stars)

if __name__ == '__main__':
    print("--- Inverted Pyramid with Base Width 9 ---")
    print_inverted_pyramid(9)