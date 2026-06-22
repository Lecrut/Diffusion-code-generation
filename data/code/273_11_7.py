def process_indices():
    indices = []
    squares = []
    for i in range(5):
        indices.append(i)
        squares.append(i ** 2)
    return indices, squares

if __name__ == '__main__':
    indices, squares = process_indices()
    print(indices)
    print(squares)