def print_star_square(size):
    rows = [['*'] * size for _ in range(size)]
    for row in rows:
        print(''.join(row))

if __name__ == '__main__':
    print_star_square(8)