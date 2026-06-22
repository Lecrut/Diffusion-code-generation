def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    test_side = 12
    area = calculate_square_area(test_side)
    print(f"The area of a square with side {test_side} is: {area}")