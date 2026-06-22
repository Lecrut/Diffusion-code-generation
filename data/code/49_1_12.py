def print_star_square(size):
    if size <= 0:
        return
    for i in range(size):
        if i == 0 or i == size - 1:
            print('*' * size)
        else:
            if size == 1:
                print('*')
            elif size == 2:
                print('**')
            else:
                print('*' + ' ' * (size - 2) + '*')

if __name__ == '__main__':
    print_star_square(5)
    print_star_square(3)
    print_star_square(1)
    print_star_square(2)