import math
def are_areas_equal(shape1, shape2):
    area1 = 0
    area2 = 0
    if shape1['type'] == 'rectangle':
        area1 = shape1['width'] * shape1['height']
    elif shape1['type'] == 'circle':
        area1 = math.pi * shape1['radius']**2
    elif shape1['type'] == 'triangle':
        area1 = 0.5 * shape1['base'] * shape1['height']
    else:
        return False
    if shape2['type'] == 'rectangle':
        area2 = shape2['width'] * shape2['height']
    elif shape2['type'] == 'circle':
        area2 = math.pi * shape2['radius']**2
    elif shape2['type'] == 'triangle':
        area2 = 0.5 * shape2['base'] * shape2['height']
    else:
        return False
    return area1 == area2
if __name__ == '__main__':
    shape_a = {'type': 'rectangle', 'width': 4, 'height': 5}
    shape_b = {'type': 'rectangle', 'width': 10, 'height': 2}
    shape_c = {'type': 'circle', 'radius': 3}
    shape_d = {'type': 'circle', 'radius': math.sqrt(3)}
    shape_e = {'type': 'triangle', 'base': 6, 'height': 4}
    shape_f = {'type': 'triangle', 'base': 8, 'height': 3}
    print(f"Area of A: {4 * 5}")
    print(f"Area of B: {10 * 2}")
    print(f"Areas of A and B are equal: {are_areas_equal(shape_a, shape_b)}")
    print(f"\nArea of C: {math.pi * 3**2}")
    print(f"Area of D: {math.pi * math.sqrt(3)**2}")
    print(f"Areas of C and D are equal: {are_areas_equal(shape_c, shape_d)}")
    print(f"\nArea of E: {0.5 * 6 * 4}")
    print(f"Area of F: {0.5 * 8 * 3}")
    print(f"Areas of E and F are equal: {are_areas_equal(shape_e, shape_f)}")