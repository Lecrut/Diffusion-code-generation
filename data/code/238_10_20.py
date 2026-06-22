def print_box():
    width = 5
    height = 3
    for y in range(height):
        for x in range(width):
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

if __name__ == '__main__':
    print_box()