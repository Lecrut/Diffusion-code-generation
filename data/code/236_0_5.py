def generate_square(size):
    square = ""
    for i in range(size):
        square += "*" * (2 * i + 1)
    return square
if __name__ == '__main__':
    num_squares = 5
    output = []
    for i in range(num_squares):
        square_size = i + 1
        generated_square = ""
        for j in range(square_size):
            generated_square += "*" * (2 * j + 1)
        output.append(generated_square)
    for s in output:
        print(s)