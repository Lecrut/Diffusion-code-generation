import math

def scale_area(shape, dimension, scale_factor):
    if shape == "rectangle":
        length, width = dimension
        scaled_length = length * scale_factor
        scaled_width = width * scale_factor
        return scaled_length * scaled_width
    elif shape == "circle":
        radius = dimension
        scaled_radius = radius * scale_factor
        return math.pi * (scaled_radius ** 2)
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rect_area = scale_area("rectangle", (10, 5), 2)
    circle_area = scale_area("circle", 7, 3)
    print(rect_area)
    print(circle_area)