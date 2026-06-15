def generate_square(size):
    for i in range(size):
        print('*' * (2 * i + 1))
if __name__ == '__main__':
    num_squares = 5
    for _ in range(num_squares):
        generate_square(5)