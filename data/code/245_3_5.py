def calculate_area(shape):
    if shape[0] is not None:
        return 3.141592653589793 * shape[0]**2
    elif len(shape) == 2:
        return shape[0] * shape[1]
    else:
        return None
def compare_areas(shape1, shape2):
    area1 = calculate_area(shape1)
    area2 = calculate_area(shape2)
    if area1 is None or area2 is None:
        return False
    return area1 == area2
if __name__ == '__main__':
    shape_a = (5, None)
    shape_b = (3, 4)
    shape_c = (7, None)
    print(f"Area of shape_a: {calculate_area(shape_a)}")
    print(f"Area of shape_b: {calculate_area(shape_b)}")
    print(f"Area of shape_c: {calculate_area(shape_c)}")
    result1 = compare_areas(shape_a, shape_b)
    print(f"Are areas of shape_a and shape_b equal? {result1}")
    result2 = compare_areas(shape_a, shape_c)
    print(f"Are areas of shape_a and shape_c equal? {result2}")
    shape_d = (3.5, None)
    shape_e = (4, 2.75)
    print(f"Area of shape_d: {calculate_area(shape_d)}")
    print(f"Area of shape_e: {calculate_area(shape_e)}")
    result3 = compare_areas(shape_d, shape_e)
    print(f"Are areas of shape_d and shape_e equal? {result3}")