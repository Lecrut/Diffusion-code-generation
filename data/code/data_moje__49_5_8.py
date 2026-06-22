def print_star_square():
    dimension = 8
    rows = [['*' for _ in range(dimension)] for _ in range(dimension)]
    for row in rows:
        print(''.join(row))

if __name__ == '__main__':
    print_star_square()