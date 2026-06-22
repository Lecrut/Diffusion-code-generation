from typing import Union

def calculate_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative numbers.")
    return length * width

if __name__ == '__main__':
    sample_values = {
        'length': 6.5,
        'width': 2.8
    }
    area = calculate_area(sample_values['length'], sample_values['width'])
    print(area)