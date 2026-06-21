from typing import Union

def calculate_rectangle_area(width: Union[int, float], height: Union[int, float]) -> Union[int, float]:
    return width * height

if __name__ == '__main__':
    area = calculate_rectangle_area(5, 10)
    print(area)