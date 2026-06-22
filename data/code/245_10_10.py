import math

SHAPES = {
    'circle': ('radius', lambda radius: math.pi * radius ** 2),
    'rectangle': ('length,width', lambda length, width: length * width)
}

def calculate_area(shape_type, dimensions):
    shape_info = SHAPES.get(shape_type)
    if not shape_info:
        raise ValueError(f"Unknown shape type: {shape_type}")
    params, area_func = shape_info
    return area_func(*dimensions)

if __name__ == '__main__':
    circle_radius = 5.0
    rectangle_length = 10.0
    rectangle_width = 5.0

    circle_area = calculate_area('circle', (circle_radius,))
    rectangle_area = calculate_area('rectangle', (rectangle_length, rectangle_width))

    if abs(circle_area - rectangle_area) < 1e-9:
        print("The areas are equal.")
    else:
        print("The areas are not equal.")