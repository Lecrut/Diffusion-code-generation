def calculate_area(dimensions):
    width, height = dimensions
    return width * height

def compare_areas(rect1, rect2):
    area1 = calculate_area(rect1)
    area2 = calculate_area(rect2)
    return area1 == area2

if __name__ == '__main__':
    rectangle1_dims = (3.0, 4.0)
    rectangle2_dims = (6.0, 2.0)
    result = compare_areas(rectangle1_dims, rectangle2_dims)
    print(f"Rectangle areas are equal: {result}")