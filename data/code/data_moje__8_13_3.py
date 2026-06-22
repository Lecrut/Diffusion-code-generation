import math

def calculate_scaled_area(shape, dimensions, scale_factor):
    if shape == "rectangle":
        width, height = dimensions
        base_area = width * height
    elif shape == "circle":
        radius = dimensions
        base_area = math.pi * (radius ** 2)
    else:
        raise ValueError("Unsupported shape: {}".format(shape))
    scaled_area = base_area * (scale_factor ** 2)
    return scaled_area

if __name__ == '__main__':
    rect_dimensions = (10.0, 5.0)
    rect_scale = 2.0
    rect_area = calculate_scaled_area("rectangle", rect_dimensions, rect_scale)
    print("Scaled Rectangle Area: {}".format(rect_area))

    circle_dimensions = 7.0
    circle_scale = 1.5
    circle_area = calculate_scaled_area("circle", circle_dimensions, circle_scale)
    print("Scaled Circle Area: {}".format(circle_area))