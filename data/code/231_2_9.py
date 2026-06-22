def print_pattern():
    for i in range(10):
        for j in range(10):
            if (i + j) % 2 == 0:
                print('*', end='')
            else:
                print('.', end='')
        print()

if __name__ == '__main__':
    print_pattern()