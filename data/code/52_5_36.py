from typing import Union

def calculate_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Length and width must be numerical values.")
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative numbers.")
    return length * width

if __name__ == '__main__':
    sample_length = 6.5
    sample_width = 2.0
    try:
        area = calculate_area(sample_length, sample_width)
        print(area)
    except ValueError as e:
        print(e)