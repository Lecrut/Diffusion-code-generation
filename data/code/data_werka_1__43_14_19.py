def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side length must be a number.")
    if side <= 0:
        raise ValueError("Side length must be a positive number.")
    return side * side

if __name__ == '__main__':
    test_values = [5, 10.5, -3, 0, 'a']
    for value in test_values:
        try:
            area = calculate_square_area(value)
            print(f"The area of a square with side {value} is: {area}")
        except (TypeError, ValueError) as e:
            print(f"Error for input {value}: {e}")