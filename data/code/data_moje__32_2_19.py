from typing import Union

Number = Union[int, float]

def calculate_rectangle_area(width: Number, height: Number) -> Number:
    return width * height

if __name__ == '__main__':
    w = 10
    h = 5
    result = calculate_rectangle_area(w, h)
    print(result)