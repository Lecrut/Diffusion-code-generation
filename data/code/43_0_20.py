def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    test_side = 5
    result = calculate_square_area(test_side)
    print(result)

    test_side = 10.5
    result = calculate_square_area(test_side)
    print(result)