import math
def check_equal_area(shape1_data, shape2_data):
    try:
        radius1 = shape1_data['radius']
        radius2 = shape2_data['radius']
        area1 = math.pi * (radius1 ** 2)
        length1 = shape1_data['length']
        width1 = shape1_data['width']
        area2 = length1 * width1
        tolerance = 1e-9
        if abs(area1 - area2) < tolerance:
            return True
        else:
            return False
    except KeyError:
        return False
    except TypeError:
        return False
if __name__ == '__main__':
    shape_a = {
        'radius': 5.0,
        'length': 10.0,
        'width': 2.0
    }
    shape_b = {
        'radius': 3.0,
        'length': 4.0,
        'width': 3.141592653589793
    }
    result1 = check_equal_area(shape_a, shape_b)
    print(f"Result 1: {result1}")
    shape_c = {
        'radius': 10.0,
        'length': 5.0,
        'width': 2.0
    }
    shape_d = {
        'radius': 6.0,
        'length': 5.0,
        'width': 2.0
    }
    result2 = check_equal_area(shape_c, shape_d)
    print(f"Result 2: {result2}")