def generate_square_star(size):
    for _ in range(size):
        yield '* ' * size

if __name__ == '__main__':
    size = 3
    for row in generate_square_star(size):
        print(row.rstrip())