def generate_star_square(size):
    return (('*' * size) for _ in range(size))

if __name__ == '__main__':
    fixed_size = 3
    for row in generate_star_square(fixed_size):
        print(row)