def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_side_lengths = [2, 5, 8]
    for length in sample_side_lengths:
        try:
            area = calculate_square_area(length)
            print(f"The area of a square with side length {length} is {area}")
        except ValueError as e:
            print(e)