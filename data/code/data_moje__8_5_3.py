import math

def calculate_area(shape_type, *dimensions):
    shape_type = shape_type.lower()
    if shape_type == "rectangle":
        if len(dimensions) != 2:
            raise ValueError("Rectangle requires width and height")
        width, height = dimensions
        return width * height
    elif shape_type == "circle":
        if len(dimensions) != 1:
            raise ValueError("Circle requires radius")
        radius = dimensions[0]
        return math.pi * (radius ** 2)
    else:
        raise ValueError(f"Unsupported shape: {shape_type}")

if __name__ == '__main__':
    print(calculate_area("rectangle", 5, 10))
    print(calculate_area("circle", 7))