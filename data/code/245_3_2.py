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
    circle_dims = (5.0, None)
    rectangle_dims = (3.0, 4.0)
    square_dims = (5.0, 5.0)
    print(f"Circle Area: {calculate_area(circle_dims)}")
    print(f"Rectangle Area: {calculate_area(rectangle_dims)}")
    print(f"Square Area: {calculate_area(square_dims)}")
    result1 = compare_areas(circle_dims, rectangle_dims)
    print(f"Circle and Rectangle areas are equal: {result1}")
    result2 = compare_areas(rectangle_dims, square_dims)
    print(f"Rectangle and Square areas are equal: {result2}")