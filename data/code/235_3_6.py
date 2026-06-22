def inverted_pyramid(base_width):
    for i in range(base_width // 2, -1, -1):
        print(' ' * (base_width // 2 - i) + '*' * (i * 2 + 1))

if __name__ == '__main__':
    inverted_pyramid(9)