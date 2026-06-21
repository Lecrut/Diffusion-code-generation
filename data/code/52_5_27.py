from typing import Union

def calculate_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Both length and width must be numbers.")
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative numbers.")
    return length * width

if __name__ == '__main__':
    try:
        sample_length = 6.5
        sample_width = 2.3
        area = calculate_area(sample_length, sample_width)
        print(area)
    except (TypeError, ValueError) as e:
        print(e)