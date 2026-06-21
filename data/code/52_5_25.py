from typing import Union
MIN_DIMENSION = 0

def calculate_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    if length < MIN_DIMENSION or width < MIN_DIMENSION:
        raise ValueError('Length and width must be non-negative numbers.')
    return length * width
if __name__ == '__main__':
    sample_length = 12.5
    sample_width = 6.0
    area_result = calculate_area(sample_length, sample_width)
    print(area_result)