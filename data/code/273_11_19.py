MAX_REPETITIONS = 5

def process_sequence():
    indices = []
    squares = []
    for i in range(MAX_REPETITIONS):
        indices.append(i)
        squares.append(i ** 2)
    return indices, squares

if __name__ == '__main__':
    indices, squares = process_sequence()
    print("Indices:", indices)
    print("Squares:", squares)