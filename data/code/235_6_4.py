def create_pyramid(levels):
    for i in range(1, levels + 1):
        spaces = ' ' * (levels - i)
        plus_signs = '+' * (2 * i - 1)
        print(spaces + plus_signs)

if __name__ == '__main__':
    create_pyramid(5)