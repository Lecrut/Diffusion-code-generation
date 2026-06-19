def calculate_square_area(side_length):
    area = side_length * side_length
    return area

if __name__ == '__main__':
    test_values = [4, 6.3, 9]
    for value in test_values:
        result = calculate_square_area(value)
        print(result)