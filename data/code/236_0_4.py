def generate_square(size):
    square = ""
    for i in range(size):
        square += "*" * (2 * i + 1)
    return square
if __name__ == '__main__':
    num_squares = 5
    all_squares = []
    for i in range(num_squares):
        square_size = i + 1
        square = ""
        for j in range(square_size):
            square += "*" * (2 * j + 1)
        all_squares.append(square)
    for square in all_squares:
        print(square)