def compute_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    test_cases = [6.2, 10, -3]
    for index, value in enumerate(test_cases):
        try:
            area_result = compute_square_area(value)
            print(f"Test case {index + 1}: The area of a square with side length {value} is {area_result}")
        except ValueError as e:
            print(f"Test case {index + 1}: Error - {e}")