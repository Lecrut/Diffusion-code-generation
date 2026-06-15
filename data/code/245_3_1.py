def calculate_area(shape):
    if shape[1] is None:
        return 3.141592653589793 * shape[0]**2
    else:
        return shape[0] * shape[1]
def compare_areas(shape1, shape2):
    area1 = calculate_area(shape1)
    area2 = calculate_area(shape2)
    return area1 == area2
if __name__ == '__main__':
    circle = (5.0, None)
    rectangle = (4.0, 12.0)
    square = (6.0, 6.0)
    print(f"Circle dimensions: {circle}")
    print(f"Rectangle dimensions: {rectangle}")
    print(f"Square dimensions: {square}")
    result1 = compare_areas(circle, rectangle)
    print(f"Area of circle vs rectangle are equal: {result1}")
    result2 = compare_areas(circle, square)
    print(f"Area of circle vs square are equal: {result2}")
    result3 = compare_areas(rectangle, square)
    print(f"Area of rectangle vs square are equal: {result3}")