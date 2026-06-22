def calculate_area(width, height):
    return width * height if height is not None else 3.141592653589793 * width**2

def validate_dimensions(dimensions):
    if dimensions[0] <= 0:
        raise ValueError("Width must be greater than zero")
    if dimensions[1] < 0:
        raise ValueError("Height must be non-negative")

def compare_areas(rectangle1, rectangle2):
    validate_dimensions(rectangle1)
    validate_dimensions(rectangle2)
    area1 = calculate_area(*rectangle1)
    area2 = calculate_area(*rectangle2)
    return area1 == area2

if __name__ == '__main__':
    rectangle1 = (3.0, 4.0)
    rectangle2 = (6.0, 2.0)
    print(f"Rectangle 1 Area: {calculate_area(*rectangle1)}")
    print(f"Rectangle 2 Area: {calculate_area(*rectangle2)}")
    result1 = compare_areas(rectangle1, rectangle2)
    print(f"Rectangle areas are equal: {result1}")