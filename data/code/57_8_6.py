def calculate_area(shape, dimensions):
    if shape == 'square':
        return dimensions['side'] ** 2
    elif shape == 'circle':
        radius = dimensions['radius']
        import math
        return math.pi * (radius ** 2)
    elif shape == 'rectangle':
        return dimensions['length'] * dimensions['width']
    else:
        raise ValueError("Unknown shape")
if __name__ == '__main__':
    shape1 = 'square'
    dimensions1 = {'side': 5}
    area1 = calculate_area(shape1, dimensions1)
    print(f"Area of {shape1}: {area1}")
    shape2 = 'circle'
    dimensions2 = {'radius': 4}
    area2 = calculate_area(shape2, dimensions2)
    print(f"Area of {shape2}: {area2}")
    shape3 = 'rectangle'
    dimensions3 = {'length': 10, 'width': 3}
    area3 = calculate_area(shape3, dimensions3)
    print(f"Area of {shape3}: {area3}")