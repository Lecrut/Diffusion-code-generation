def calculate_area(side):
    return side * side

if __name__ == '__main__':
    test_side = 12
    area = calculate_area(test_side)
    print(f"The area of a square with side {test_side} is {area}")