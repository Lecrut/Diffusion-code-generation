def print_square_star_pattern(size=6):
    line = '*' * size
    for _ in range(size):
        print(line)

if __name__ == '__main__':
    print_square_star_pattern()