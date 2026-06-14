import math
def are_areas_equal(shape1, shape2):
    area1 = 0
    area2 = 0
    if shape1.get('type') == 'rectangle':
        length = shape1.get('length', 0)
        width = shape1.get('width', 0)
        area1 = length * width
    elif shape1.get('type') == 'circle':
        radius = shape1.get('radius', 0)
        area1 = math.pi * (radius ** 2)
    elif shape1.get('type') == 'triangle':
        base = shape1.get('base', 0)
        height = shape1.get('height', 0)
        area1 = 0.5 * base * height
    if shape2.get('type') == 'rectangle':
        length = shape2.get('length', 0)
        width = shape2.get('width', 0)
        area2 = length * width
    elif shape2.get('type') == 'circle':
        radius = shape2.get('radius', 0)
        area2 = math.pi * (radius ** 2)
    elif shape2.get('type') == 'triangle':
        base = shape2.get('base', 0)
        height = shape2.get('height', 0)
        area2 = 0.5 * base * height
    return area1 == area2
if __name__ == '__main__':
    shape_a = {'type': 'rectangle', 'length': 4, 'width': 5}
    shape_b = {'type': 'rectangle', 'length': 10, 'width': 2}
    shape_c = {'type': 'circle', 'radius': 3}
    shape_d = {'type': 'circle', 'radius': 2}
    shape_e = {'type': 'triangle', 'base': 6, 'height': 4}
    shape_f = {'type': 'triangle', 'base': 8, 'height': 3}
    print(f"Areas of Rectangle (4x5=20 and 10x2=20): {are_areas_equal(shape_a, shape_b)}")
    print(f"Areas of Circle (r=3 vs r=2): {are_areas_equal(shape_c, shape_d)}")
    print(f"Areas of Triangle (6x4=12 and 8x3=12): {are_areas_equal(shape_e, shape_f)}")
    print(f"Areas of Rectangle (4x5=20 vs Circle r=2.565): {are_areas_equal(shape_a, shape_c)}")