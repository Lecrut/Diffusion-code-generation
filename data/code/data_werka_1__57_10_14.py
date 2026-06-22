import math

def calculate_area(shape, **kwargs):
    area_functions = {
        'circle': lambda r: math.pi * r ** 2,
        'triangle': lambda b, h: 0.5 * b * h
    }
    if shape in area_functions:
        return area_functions[shape](**kwargs)
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    shape1 = 'circle'
    radius = 3
    area_circle = calculate_area(shape1, r=radius)
    print(area_circle)

    shape2 = 'triangle'
    base = 6
    height = 2
    area_triangle = calculate_area(shape2, b=base, h=height)
    print(area_triangle)