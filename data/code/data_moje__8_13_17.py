import math

def calculate_scaled_area(shape_type, dimensions, scale_factor):
    if shape_type == "rectangle":
        length, width = dimensions
        base_area = length * width
    elif shape_type == "circle":
        radius = dimensions
        base_area = math.pi * radius ** 2
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")
    scaled_area = base_area * (scale_factor ** 2)
    return scaled_area

if __name__ == '__main__':
    rect_area = calculate_scaled_area("rectangle", (5.0, 10.0), 2.0)
    print(rect_area)
    circle_area = calculate_scaled_area("circle", 7.0, 3.0)
    print(circle_area)