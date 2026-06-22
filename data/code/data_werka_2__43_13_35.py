SQUARE_UNIT = "square units"

def compute_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    sample_values = [2.5, 10, 0]
    for value in sample_values:
        try:
            area = compute_square_area(value)
            print(f"The area of a square with side length {value} is {area} {SQUARE_UNIT}")
        except ValueError as e:
            print(e)