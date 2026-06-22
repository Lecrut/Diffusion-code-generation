def print_star_square(size):
    if size <= 0:
        print()
        return
    for i in range(size):
        if i == 0 or i == size - 1:
            print('*' * size)
        else:
            print('*' + ' ' * (size - 2) + '*')

if __name__ == '__main__':
    print_star_square(5)
    print()
    print_star_square(3)
    print()
    print_star_square(1)
    print()
    print_star_square(0)
    print()
    print_star_square(4)