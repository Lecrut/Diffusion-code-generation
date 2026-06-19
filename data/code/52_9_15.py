from typing import Union

def calculate_area(length: float, width: float) -> float:
    return length * width

if __name__ == '__main__':
    rectangle_length = 12.5
    rectangle_width = 4.0
    area_result = calculate_area(rectangle_length, rectangle_width)
    print(f"The area of the rectangle is: {area_result}")