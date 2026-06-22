def print_squares_up_to(limit):
    squares = {i: i**2 for i in range(1, limit + 1)}
    for square in squares.values():
        print(square)

if __name__ == '__main__':
    print_squares_up_to(10)