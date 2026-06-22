def print_square_stars(side_length):
    for _ in range(side_length):
        print('*' * side_length)

if __name__ == '__main__':
    side = 5
    print_square_stars(side)