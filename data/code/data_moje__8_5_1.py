import math

def calculate_area(shape_type, *dimensions):
    if shape_type == "rectangle":
        if len(dimensions) != 2:
            raise ValueError("Rectangle requires exactly two dimensions: width and height")
        width, height = dimensions
        return width * height
    elif shape_type == "circle":
        if len(dimensions) != 1:
            raise ValueError("Circle requires exactly one dimension: radius")
        radius = dimensions[0]
        return math.pi * (radius ** 2)
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    rect_area = calculate_area("rectangle", 5, 10)
    print(rect_area)

    circle_area = calculate_area("circle", 7)
    print(circle_area)