MIN_SIDE_LENGTH = 0

def calculate_square_area(side_length):
    if side_length < MIN_SIDE_LENGTH:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_values = [4, 7.2, MIN_SIDE_LENGTH, -3]
    for value in sample_values:
        try:
            area = calculate_square_area(value)
            print(f"The area of a square with side length {value} is {area}")
        except ValueError as e:
            print(e)