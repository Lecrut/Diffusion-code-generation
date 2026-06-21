def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_values = {
        'tiny': 1,
        'small': 4,
        'medium': 6,
        'large': 9
    }
    for size, value in sample_values.items():
        try:
            area = calculate_square_area(value)
            print(f"The area of a {size} square with side length {value} is {area}")
        except ValueError as e:
            print(e)