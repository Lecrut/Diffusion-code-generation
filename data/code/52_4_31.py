from typing import Union

def calculate_area_square(side_length: float) -> float:
    if side_length < 0:
        raise ValueError('Side length cannot be negative')
    return side_length * side_length

def calculate_area_rectangle(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError('Length and width cannot be negative')
    return length * width

def calculate_area_circle(radius: float) -> float:
    import math
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return math.pi * radius * radius

SHAPE_AREAS = {
    'square': calculate_area_square,
    'rectangle': calculate_area_rectangle,
    'circle': calculate_area_circle
}

def calculate_area(shape: str, **kwargs) -> float:
    area_func = SHAPE_AREAS.get(shape)
    if not area_func:
        raise ValueError(f"Unsupported shape: {shape}")
    return area_func(**kwargs)

if __name__ == '__main__':
    print(calculate_area('square', side_length=5.0))
    print(calculate_area('rectangle', length=4.0, width=6.0))
    print(calculate_area('circle', radius=3.0))