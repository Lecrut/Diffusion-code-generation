from typing import Union

def calculate_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative numbers.")
    return length * width

if __name__ == '__main__':
    sample_length = 8
    sample_width = 3.5
    area = calculate_area(sample_length, sample_width)
    print(area)