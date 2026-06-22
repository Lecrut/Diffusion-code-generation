def generate_star_square(size):
    return ['*' * size for _ in range(size)]

if __name__ == '__main__':
    square_size = 3
    print('\n'.join(generate_star_square(square_size)))