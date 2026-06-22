def print_solid_square(side_length):
    for i in range(side_length):
        for j in range(side_length):
            print('*', end='')
        print()

if __name__ == '__main__':
    print_solid_square(5)