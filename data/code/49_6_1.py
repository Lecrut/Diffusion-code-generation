import itertools

def print_square_of_stars(size):
    lines = itertools.repeat("*" * size)
    for _ in range(size):
        print(next(lines))

if __name__ == '__main__':
    print_square_of_stars(10)