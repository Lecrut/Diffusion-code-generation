def generate_star_square(size):
    for row in range(size):
        yield '*' * size

if __name__ == '__main__':
    for line in generate_star_square(10):
        print(line)