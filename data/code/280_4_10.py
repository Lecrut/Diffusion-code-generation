def print_squares():
    squares = {i: i ** 2 for i in range(1, 21)}
    for number, square in squares.items():
        print(f'{number}: {square}')

if __name__ == '__main__':
    print_squares()