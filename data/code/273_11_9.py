MAX_ITERATIONS = 5

def process_indices():
    indices = []
    squares = []
    for i in range(MAX_ITERATIONS):
        indices.append(i)
        squares.append(i ** 2)
    return indices, squares

if __name__ == '__main__':
    indices, squares = process_indices()
    print("Indices:", indices)
    print("Squares:", squares)