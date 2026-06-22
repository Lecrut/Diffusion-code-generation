def print_grid(size=15):
    for i in range(size):
        for j in range(size):
            if j > 0:
                print(' | ', end='')
            print('*', end='')
        print()

if __name__ == '__main__':
    print_grid()