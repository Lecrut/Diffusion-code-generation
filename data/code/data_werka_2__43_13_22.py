def compute_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    test_values = [4.5, 7, -1]
    for value in test_values:
        try:
            area = compute_square_area(value)
            print(f"The area of a square with side length {value} is {area}")
        except ValueError as e:
            print(e)