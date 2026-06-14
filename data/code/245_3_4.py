import math
def calculate_area(shape):
    if shape[1] is None:
        return math.pi * shape[0]**2
    else:
        return shape[0] * shape[1]
def are_areas_equal(shape1, shape2):
    area1 = calculate_area(shape1)
    area2 = calculate_area(shape2)
    return area1 == area2
if __name__ == '__main__':
    shape_circle = (5.0, None)
    shape_rectangle = (10.0, 2.0)
    print(f"Shape 1: {shape_circle}, Area: {calculate_area(shape_circle)}")
    print(f"Shape 2: {shape_rectangle}, Area: {calculate_area(shape_rectangle)}")
    result = are_areas_equal(shape_circle, shape_rectangle)
    print(f"Are the areas equal? {result}")
    shape_circle_2 = (10.0, None)
    print(f"\nShape 1: {shape_circle_2}, Area: {calculate_area(shape_circle_2)}")
    print(f"Shape 2: {shape_rectangle}, Area: {calculate_area(shape_rectangle)}")
    result_2 = are_areas_equal(shape_circle_2, shape_rectangle)
    print(f"Are the areas equal? {result_2}")