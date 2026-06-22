def calculate_square_area(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive.")
    return side_length ** 2

if __name__ == '__main__':
    test_cases = [5, -3, 0, None, "10"]
    for value in test_cases:
        try:
            area_value = calculate_square_area(value)
            print(f"Side length: {value}")
            print(f"Area of square: {area_value}\n")
        except ValueError as e:
            print(f"Error calculating area for side {value}: {e}")