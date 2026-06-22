from typing import Union

def validate_dimensions(length: Union[int, float], width: Union[int, float]) -> None:
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numbers.")
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative numbers.")

def calculate_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    validate_dimensions(length, width)
    return length * width

if __name__ == '__main__':
    sample_length = 6.5
    sample_width = 2.0
    area = calculate_area(sample_length, sample_width)
    print(area)