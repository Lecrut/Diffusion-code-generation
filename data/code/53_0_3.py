def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)) or side_length < 0:
        raise ValueError("Side length must be a non-negative number.")
    return side_length * side_length

if __name__ == '__main__':
    sample_side_lengths = [2.5, 4, 0, -1]
    for length in sample_side_lengths:
        try:
            area = calculate_square_area(length)
            print(f"The area of a square with side length {length} is {area}.")
        except ValueError as e:
            print(e)