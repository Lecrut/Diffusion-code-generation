def repeat_operations():
    indices = []
    squares = []

    for i in range(5):
        indices.append(i)
        squares.append(i ** 2)

    return indices, squares

if __name__ == '__main__':
    result_indices, result_squares = repeat_operations()
    print(result_indices)
    print(result_squares)