def process_indices():
    indices = []
    squares = []
    for i in range(5):
        indices.append(i)
        squares.append(i ** 2)
    return indices, squares

if __name__ == '__main__':
    try:
        indices, squares = process_indices()
        print("Indices:", indices)
        print("Squares:", squares)
    except Exception as e:
        print(f"An error occurred: {e}")