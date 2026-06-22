def generate_squares(limit):
    squares = []
    for i in range(limit):
        squares.append(i**2)
    return squares

if __name__ == '__main__':
    sample_limit = 10
    result = generate_squares(sample_limit)
    print(result)