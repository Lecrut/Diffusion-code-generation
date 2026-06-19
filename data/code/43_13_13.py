def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    test_side_length = 6
    area_result = calculate_square_area(test_side_length)
    print(f"The area of the square with side length {test_side_length} is: {area_result}")