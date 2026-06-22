indices_squares_map = {i: i ** 2 for i in range(5)}

def append_index_and_square():
    indices = []
    squares = []
    for index, _ in enumerate(indices_squares_map):
        indices.append(index)
        squares.append(indices_squares_map[index])
    return indices, squares

if __name__ == '__main__':
    indices, squares = append_index_and_square()
    print("Indices:", indices)
    print("Squares:", squares)