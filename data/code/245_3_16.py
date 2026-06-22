def calculate_area(width, height):
    if width < 0 or height < 0:
        raise ValueError('Width and height must be non-negative numbers.')
    return width * height

def compare_areas(rect1, rect2):
    area1 = calculate_area(*rect1)
    area2 = calculate_area(*rect2)
    return area1 == area2
if __name__ == '__main__':
    circle_dims = (5.0, 0)
    rectangle_dims = (3.0, 4.0)
    square_dims = (5.0, 5.0)
    print(f'Circle Area: {calculate_area(*circle_dims)}')
    print(f'Rectangle Area: {calculate_area(*rectangle_dims)}')
    print(f'Square Area: {calculate_area(*square_dims)}')
    result1 = compare_areas(circle_dims, rectangle_dims)
    print(f'Circle and Rectangle areas are equal: {result1}')