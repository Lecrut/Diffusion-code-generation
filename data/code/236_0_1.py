def generate_square(size):
    square = ""
    for i in range(size):
        square += "*" * (2 * i + 1)
        square += "\n"
    return square
if __name__ == '__main__':
    num_squares = 5
    all_squares = []
    for i in range(num_squares):
        square_size = i + 1
        square_output = ""
        for j in range(square_size):
            row = ""
            for k in range(square_size):
                if j == k:
                    row += "*"
                else:
                    row += " "
            square_output += row + "\n"
        all_squares.append(square_output)
    for sq in all_squares:
        print(sq)