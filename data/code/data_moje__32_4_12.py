from typing import Union

def calculate_rectangle_area(width: Union[int, float], height: Union[int, float]) -> float:
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numbers")
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")
    return width * height

if __name__ == '__main__':
    sample_width = 10
    sample_height = 5
    result = calculate_rectangle_area(sample_width, sample_height)
    print(result)