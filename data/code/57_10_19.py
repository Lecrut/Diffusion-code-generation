import math

def calculate_area(shape, **kwargs):
    if shape == 'circle':
        return math.pi * kwargs['radius'] ** 2
    elif shape == 'triangle':
        return 0.5 * kwargs['base'] * kwargs['height']
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    shape1 = 'circle'
    radius = 3
    area_circle = calculate_area(shape1, radius=radius)
    print(area_circle)

    shape2 = 'triangle'
    base = 6
    height = 2
    area_triangle = calculate_area(shape2, base=base, height=height)
    print(area_triangle)