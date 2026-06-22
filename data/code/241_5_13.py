def validate_dimensions(length: float, width: float) -> None:
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers")

def rectangle_area(length: float, width: float) -> float:
    validate_dimensions(length, width)
    return length * width

if __name__ == '__main__':
    sample_length = 5.0
    sample_width = 10.0
    area = rectangle_area(sample_length, sample_width)
    print(f"The area of the rectangle with length {sample_length} and width {sample_width} is {area}")