def validate_side_length(side: float) -> bool:
    return side > 0

def calculate_square_area(side: float) -> float:
    if not validate_side_length(side):
        raise ValueError("Side length must be positive")
    return side * side

if __name__ == '__main__':
    sample_values = [3.5, 7.2, 10]
    for side_value in sample_values:
        area = calculate_square_area(side_value)
        print(f"The area of the square with side {side_value} is {area}")