from typing import Union

def calculate_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    return length * width

if __name__ == '__main__':
    sample_length = 5.0
    sample_width = 3.0
    area = calculate_area(sample_length, sample_width)
    print(area)