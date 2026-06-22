import math

def calculate_scaled_area(shape, dimensions, scale_factor):
    if shape == "rectangle":
        if len(dimensions) != 2:
            raise ValueError("Rectangle requires exactly two dimensions: length and width")
        length, width = dimensions
        scaled_length = length * scale_factor
        scaled_width = width * scale_factor
        return scaled_length * scaled_width
    elif shape == "circle":
        if len(dimensions) != 1:
            raise ValueError("Circle requires exactly one dimension: radius")
        radius = dimensions[0]
        scaled_radius = radius * scale_factor
        return math.pi * (scaled_radius ** 2)
    else:
        raise ValueError("Unsupported shape. Use 'rectangle' or 'circle'.")

if __name__ == '__main__':
    rect_result = calculate_scaled_area("rectangle", [10, 5], 2)
    print(rect_result)
    circle_result = calculate_scaled_area("circle", [3], 3)
    print(circle_result)