def generate_square(size):
    square = ""
    for i in range(size):
        square += "*" * (2 * i + 1)
    return square
if __name__ == '__main__':
    num_squares = 5
    all_squares = []
    for i in range(num_squares):
        side_length = i + 1
        square = ""
        for j in range(side_length):
            square += "*" * side_length
        all_squares.append(square)
    for square in all_squares:
        print(square)