def print_squares_sequence(n):
    SQUARES = [i**2 for i in range(1, n+1)]
    for square in SQUARES:
        print(square)

if __name__ == '__main__':
    print_squares_sequence(5)