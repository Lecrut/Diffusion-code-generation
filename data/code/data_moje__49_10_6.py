def print_square_pattern():
    side_length = 5
    row = '*' * side_length
    for _ in range(side_length):
        print(row)

if __name__ == '__main__':
    print_square_pattern()