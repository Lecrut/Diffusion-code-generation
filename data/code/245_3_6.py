def calculate_area(shape):
    if shape[1] is None:
        return 3.141592653589793 * shape[0]**2
    else:
        return shape[0] * shape[1]
def are_areas_equal(shape1, shape2):
    area1 = calculate_area(shape1)
    area2 = calculate_area(shape2)
    return area1 == area2
if __name__ == '__main__':
    shape_circle = (5.0, None)
    shape_rectangle = (3.0, 4.0)
    shape_other_circle = (5.0, None)
    print(f"Shape 1: {shape_circle}, Area: {calculate_area(shape_circle)}")
    print(f"Shape 2: {shape_rectangle}, Area: {calculate_area(shape_rectangle)}")
    print(f"Shape 3: {shape_other_circle}, Area: {calculate_area(shape_other_circle)}")
    result1 = are_areas_equal(shape_circle, shape_rectangle)
    print(f"Are the areas of Shape 1 and Shape 2 equal? {result1}")
    result2 = are_areas_equal(shape_circle, shape_other_circle)
    print(f"Are the areas of Shape 1 and Shape 3 equal? {result2}")