import math
def compare_areas(shape1, shape2):
    area1 = 0
    area2 = 0
    if shape1['type'] == 'rectangle':
        length = shape1['length']
        width = shape1['width']
        area1 = length * width
    elif shape1['type'] == 'circle':
        radius = shape1['radius']
        area1 = math.pi * (radius ** 2)
    elif shape1['type'] == 'triangle':
        base = shape1['base']
        height = shape1['height']
        area1 = 0.5 * base * height
    else:
        return False
    if shape2['type'] == 'rectangle':
        length = shape2['length']
        width = shape2['width']
        area2 = length * width
    elif shape2['type'] == 'circle':
        radius = shape2['radius']
        area2 = math.pi * (radius ** 2)
    elif shape2['type'] == 'triangle':
        base = shape2['base']
        height = shape2['height']
        area2 = 0.5 * base * height
    else:
        return False
    return area1 == area2
if __name__ == '__main__':
    shape_a = {'type': 'rectangle', 'length': 4, 'width': 5}
    shape_b = {'type': 'rectangle', 'length': 10, 'width': 2}
    shape_c = {'type': 'circle', 'radius': 3}
    shape_d = {'type': 'circle', 'radius': 2}
    shape_e = {'type': 'triangle', 'base': 6, 'height': 4}
    shape_f = {'type': 'triangle', 'base': 8, 'height': 3}
    print(f"Area of A: {4 * 5}")
    print(f"Area of B: {10 * 2}")
    print(f"Areas are equal (A vs B): {compare_areas(shape_a, shape_b)}")
    print(f"\nArea of C: {math.pi * 3**2}")
    print(f"Area of D: {math.pi * 2**2}")
    print(f"Areas are equal (C vs D): {compare_areas(shape_c, shape_d)}")
    print(f"\nArea of E: {0.5 * 6 * 4}")
    print(f"Area of F: {0.5 * 8 * 3}")
    print(f"Areas are equal (E vs F): {compare_areas(shape_e, shape_f)}")