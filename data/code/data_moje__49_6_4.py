def print_stars_square(size=10):
    line = '*' * size
    for _ in range(size):
        print(line)

if __name__ == '__main__':
    print_stars_square(10)