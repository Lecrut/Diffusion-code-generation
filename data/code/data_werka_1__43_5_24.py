from typing import Union

def calculate_square_area(side_length: Union[int, float]) -> Union[int, float]:
    return side_length * side_length

if __name__ == '__main__':
    sample_side_length = 5
    area = calculate_square_area(sample_side_length)
    print(area)