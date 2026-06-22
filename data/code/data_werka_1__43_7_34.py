def calculate_square_area(side: float) -> float:
    return side * side

if __name__ == '__main__':
    test_side_length = 6.0
    calculated_area = calculate_square_area(test_side_length)
    print(f"The area of the square with side {test_side_length} is {calculated_area}")