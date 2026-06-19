def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number.")
    if side_length < 0:
        raise ValueError("Side length must be non-negative.")
    return side_length * side_length

if __name__ == '__main__':
    test_values = [3.5, 7, 0, -2]
    for value in test_values:
        try:
            area = calculate_square_area(value)
            print(f"The area of a square with side length {value} is {area}.")
        except (TypeError, ValueError) as e:
            print(e)