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
if __name__ == '__main__':
    shape_a = {
        'radius': 5.0,
        'length': 4.0,
        'width': 3.141592653589793                                             
    }
    shape_b = {
        'radius': 3.0,
        'length': 2.0,
        'width': 1.5707963267948966                                            
    }
    result1 = check_equal_area(shape_a, shape_b)
    print(f"Test Case 1: Areas are equal: {result1}")
    shape_c = {
        'radius': 5.0,
        'length': 4.0,
        'width': 3.0                                                   
    }
    result2 = check_equal_area(shape_a, shape_c)
    print(f"Test Case 2: Areas are equal: {result2}")
    shape_d = {
        'radius': 10.0,
        'length': 3.141592653589793 / 2.0,                                       
        'width': 0.0
    }
    result3 = check_equal_area(shape_a, shape_d)
    print(f"Test Case 3: Areas are equal: {result3}")