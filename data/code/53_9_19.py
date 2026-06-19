def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length must be a non-negative number.")
    return side_length * side_length

if __name__ == '__main__':
    test_values = [2, 4, 6]
    for value in test_values:
        area = calculate_square_area(value)
        print(f"The area of a square with side length {value} is {area}.")