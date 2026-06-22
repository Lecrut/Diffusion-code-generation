def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    sample_values = {
        'small': 3,
        'medium': 5.5,
        'zero': 0,
        'negative': -2
    }
    for label, value in sample_values.items():
        try:
            area = calculate_square_area(value)
            print(f"The area of a square with {label} side length {value} is {area}")
        except ValueError as e:
            print(e)