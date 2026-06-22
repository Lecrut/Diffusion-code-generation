def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_side_lengths = [4.5, 6, -1]
    for length in sample_side_lengths:
        try:
            area = calculate_square_area(length)
            print(f"The area of a square with side length {length} is {area}")
        except (TypeError, ValueError) as e:
            print(e)