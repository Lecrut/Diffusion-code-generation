def compute_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    area = side_length * side_length
    return area

if __name__ == '__main__':
    sample_values = [6.2, 9, -3]
    for value in sample_values:
        try:
            result = compute_square_area(value)
            print(f"The area of a square with side length {value} is {result}")
        except ValueError as e:
            print(e)