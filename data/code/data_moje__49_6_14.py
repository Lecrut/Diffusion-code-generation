def print_star_square(size):
    for i in range(size):
        for j in range(size):
            print('*', end='')
        print()

if __name__ == '__main__':
    print_star_square(10)