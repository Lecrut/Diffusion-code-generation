def validate_dimensions(length: float, width: float) -> None:
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers")

def calculate_area(length: float, width: float) -> float:
    return length * width

if __name__ == '__main__':
    sample_length = 5.0
    sample_width = 10.0
    validate_dimensions(sample_length, sample_width)
    area = calculate_area(sample_length, sample_width)
    print(area)