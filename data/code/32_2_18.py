from typing import Union

def _validate_positive_dimension(value: Union[int, float]) -> None:
    if not isinstance(value, (int, float)):
        raise TypeError("Dimensions must be numeric")
    if value <= 0:
        raise ValueError("Dimensions must be positive")

def calculate_rectangle_area(width: float, height: float) -> float:
    _validate_positive_dimension(width)
    _validate_positive_dimension(height)
    return width * height

if __name__ == '__main__':
    WIDTH_VALUE = 7.5
    HEIGHT_VALUE = 12.0
    area_result = calculate_rectangle_area(WIDTH_VALUE, HEIGHT_VALUE)
    print(area_result)