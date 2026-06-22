def print_square_stars(size=12):
    line = ' '.join(['*'] * size)
    for _ in range(size):
        print(line)

if __name__ == '__main__':
    print_square_stars(12)