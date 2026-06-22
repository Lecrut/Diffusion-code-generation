from typing import Union
UNIT_SCALING_FACTOR = 1.0

def calculate_area(length: Union[int, float], width: Union[int, float]) -> float:
    return length * width * UNIT_SCALING_FACTOR
if __name__ == '__main__':
    sample_length = 12.0
    sample_width = 8.5
    calculated_area = calculate_area(sample_length, sample_width)
    print(f'The area of the rectangle with length {sample_length} and width {sample_width} is: {calculated_area}')