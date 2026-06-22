def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    test_cases = [4, 6.2, -3, 0]
    for case in test_cases:
        try:
            result = calculate_square_area(case)
            print(f"The area of a square with side length {case} is {result}")
        except ValueError as e:
            print(e)