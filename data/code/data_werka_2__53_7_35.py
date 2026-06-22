def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    sample_values = {
        'tiny': 1,
        'average': 4.5,
        'large': 10,
        'edge_case_zero': 0,
        'invalid_negative': -3
    }
    for label, value in sample_values.items():
        try:
            area = calculate_square_area(value)
            print(f"The area of a square with {label} side length {value} is {area}")
        except ValueError as e:
            print(e)