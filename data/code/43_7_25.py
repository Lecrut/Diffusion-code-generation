def calculate_square_area(side_length: float) -> float:
    return side_length * side_length

if __name__ == '__main__':
    sample_values = {
        'tiny': 2.0,
        'small': 4.5,
        'medium': 6.0,
        'large': 8.0
    }
    for description, value in sample_values.items():
        area = calculate_square_area(value)
        print(f"The area of the {description} square with side {value} is {area}")