def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    test_side_length = 8.5
    computed_area = calculate_square_area(test_side_length)
    print(computed_area)