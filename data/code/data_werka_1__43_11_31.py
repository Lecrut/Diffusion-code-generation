def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    test_values = [3.5, 7, 12]
    for value in test_values:
        print(calculate_square_area(value))