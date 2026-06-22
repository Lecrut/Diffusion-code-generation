def calculate_area(side_length):
    area = side_length * side_length
    return area

if __name__ == '__main__':
    test_side = 12
    computed_area = calculate_area(test_side)
    print(f"The area of a square with side {test_side} is: {computed_area}")