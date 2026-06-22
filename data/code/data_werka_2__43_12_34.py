def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length ** 2

if __name__ == '__main__':
    sample_values = {
        'tiny': 1.5,
        'standard': 4,
        'huge': 100
    }
    for description, value in sample_values.items():
        try:
            area = calculate_square_area(value)
            print(f"The area of a {description} square with side length {value} is {area}")
        except (TypeError, ValueError) as e:
            print(e)