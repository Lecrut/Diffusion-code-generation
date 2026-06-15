import math
def check_equal_area(shape1_data, shape2_data):
    try:
        area1 = 0
        if 'radius' in shape1_data:
            area1 = math.pi * (shape1_data['radius'])**2
        elif 'length' in shape1_data and 'width' in shape1_data:
            area1 = shape1_data['length'] * shape1_data['width']
        area2 = 0
        if 'radius' in shape2_data:
            area2 = math.pi * (shape2_data['radius'])**2
        elif 'length' in shape2_data and 'width' in shape2_data:
            area2 = shape2_data['length'] * shape2_data['width']
        return abs(area1 - area2) < 1e-9
    except Exception:
        return False
if __name__ == '__main__':
    shape_a = {'type': 'circle', 'radius': 5.0}
    shape_b = {'type': 'rectangle', 'length': 5.0, 'width': 2.0}
    print(f"Checking {shape_a} and {shape_b}: {check_equal_area(shape_a, shape_b)}")
    shape_c = {'type': 'circle', 'radius': 3.0}
    shape_d = {'type': 'rectangle', 'length': 3.0, 'width': math.pi}
    print(f"Checking {shape_c} and {shape_d}: {check_equal_area(shape_c, shape_d)}")
    shape_e = {'type': 'circle', 'radius': 10.0}
    shape_f = {'type': 'rectangle', 'length': 5.0, 'width': 8.0}
    print(f"Checking {shape_e} and {shape_f}: {check_equal_area(shape_e, shape_f)}")