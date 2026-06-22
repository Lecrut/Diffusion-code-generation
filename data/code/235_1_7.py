def print_square_box(size):
    pattern = {'#': size * '#'}
    for _ in range(size):
        print(pattern['#'])

if __name__ == '__main__':
    print_square_box(4)