def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    test_values = [2, 7.8, -1, 0]
    for value in test_values:
        try:
            area = calculate_square_area(value)
            print(f"Area of square with side {value}: {area}")
        except ValueError as e:
            print(e)