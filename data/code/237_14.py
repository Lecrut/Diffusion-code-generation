def generate_perfect_squares(limit):
    squares = []
    n = 1
    while n * n <= limit:
        squares.append(n * n)
        n += 1
    return squares
if __name__ == '__main__':
    limit_value = 100
    result = generate_perfect_squares(limit_value)
    print(result)