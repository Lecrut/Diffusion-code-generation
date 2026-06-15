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
    shapeA = (5.0, None)
    shapeB = (3.0, 4.0)
    shapeC = (3.5, None)
    print(f"Area of shapeA: {calculate_area(shapeA)}")
    print(f"Area of shapeB: {calculate_area(shapeB)}")
    print(f"Area of shapeC: {calculate_area(shapeC)}")
    result1 = compare_areas(shapeA, shapeB)
    print(f"Are areas of shapeA and shapeB equal? {result1}")
    result2 = compare_areas(shapeA, shapeC)
    print(f"Are areas of shapeA and shapeC equal? {result2}")
    shapeD = (5.0, 2.0)
    result3 = compare_areas(shapeB, shapeD)
    print(f"Are areas of shapeB and shapeD equal? {result3}")