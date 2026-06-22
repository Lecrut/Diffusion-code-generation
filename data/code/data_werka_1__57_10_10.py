import math

def calculate_area(shape, **kwargs):
    areas = {
        'circle': lambda r: math.pi * r ** 2,
        'triangle': lambda b, h: 0.5 * b * h
    }
    return areas.get(shape)(**kwargs)

if __name__ == '__main__':
    shape1 = 'circle'
    radius = 7
    area_circle = calculate_area(shape1, r=radius)
    print(area_circle)
    
    shape2 = 'triangle'
    base = 8
    height = 3
    area_triangle = calculate_area(shape2, b=base, h=height)
    print(area_triangle)