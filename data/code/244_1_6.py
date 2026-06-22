def calculate_rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative.")
    return width * height

def calculate_triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return 0.5 * base * height

def sum_areas(rectangle_width, rectangle_height, triangle_base, triangle_height):
    rectangle_area = calculate_rectangle_area(rectangle_width, rectangle_height)
    triangle_area = calculate_triangle_area(triangle_base, triangle_height)
    total_area = rectangle_area + triangle_area
    return total_area

if __name__ == '__main__':
    rectangle_width = 10
    rectangle_height = 6
    triangle_base = 8
    triangle_height = 5
    result = sum_areas(rectangle_width, rectangle_height, triangle_base, triangle_height)
    print(result)