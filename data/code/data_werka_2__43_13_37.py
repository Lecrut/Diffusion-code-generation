def compute_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    test_cases = [2.5, 10, -3]
    for case in test_cases:
        try:
            area = compute_square_area(case)
            print(f"The area of a square with side length {case} is {area}")
        except ValueError as e:
            print(e)