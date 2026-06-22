def print_star_square(size):
    return [('*' * size) for _ in range(size)]

if __name__ == '__main__':
    dimension = 8
    rows = print_star_square(dimension)
    for row in rows:
        print(row)