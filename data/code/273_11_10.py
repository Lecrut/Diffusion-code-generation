def process_sequence():
    indices = []
    squares = []
    for i in range(5):
        indices.append(i)
        squares.append(i ** 2)
    return indices, squares

if __name__ == '__main__':
    result_indices, result_squares = process_sequence()
    print("Indices:", result_indices)
    print("Squares:", result_squares)