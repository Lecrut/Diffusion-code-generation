from typing import Union
SHAPE_TYPES = {'square': 'calculate_area_square', 'rectangle': 'calculate_area_rectangle', 'circle': 'calculate_area_circle', 'triangle': 'calculate_area_triangle'}

def calculate_area_square(side_length: float) -> float:
    return side_length * side_length

def calculate_area_rectangle(length: float, width: float) -> float:
    return length * width

def calculate_area_circle(radius: float) -> float:
    import math
    return math.pi * radius * radius

def calculate_area_triangle(base: float, height: float) -> float:
    return 0.5 * base * height

def calculate_area(shape_type: str, **kwargs) -> Union[float, None]:
    shape_function = SHAPE_TYPES.get(shape_type)
    if shape_function:
        return globals()[shape_function](**kwargs)
    return None
if __name__ == '__main__':
    square_side = 4.0
    rectangle_length = 5.0
    rectangle_width = 3.0
    circle_radius = 7.0
    triangle_base = 6.0
    triangle_height = 4.0
    print('Area of Square:', calculate_area('square', side_length=square_side))
    print('Area of Rectangle:', calculate_area('rectangle', length=rectangle_length, width=rectangle_width))
    print('Area of Circle:', calculate_area('circle', radius=circle_radius))
    print('Area of Triangle:', calculate_area('triangle', base=triangle_base, height=triangle_height))