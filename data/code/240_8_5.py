def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    test_cases = [5, 0, 100, 2.5]
    for case in test_cases:
        print(f"The area of a square with side length {case} is {calculate_square_area(case)}")