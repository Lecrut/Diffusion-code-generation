from typing import Union

def calculate_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative numbers.")
    return length * width

if __name__ == '__main__':
    SAMPLE_LENGTH = 6
    SAMPLE_WIDTH = 2.5
    area = calculate_area(SAMPLE_LENGTH, SAMPLE_WIDTH)
    print(area)