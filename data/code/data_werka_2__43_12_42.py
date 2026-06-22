MIN_SIDE_LENGTH = 0

def calculate_square_area(side_length):
    if side_length < MIN_SIDE_LENGTH:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_side_lengths = [4, 9, 15]
    for length in sample_side_lengths:
        try:
            area = calculate_square_area(length)
            print(f"The area of a square with side length {length} is {area}")
        except ValueError as e:
            print(e)