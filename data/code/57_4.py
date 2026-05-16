import math
def calculate_area(shape, dimensions):
    if shape == "rectangle":
        length, width = dimensions
        return length * width
    elif shape == "circle":
        radius = dimensions
        return math.pi * (radius ** 2)
    elif shape == "triangle":
        base, height = dimensions
        return 0.5 * base * height
    else:
        return None
if __name__ == '__main__':
    shape_type = "rectangle"
    dimensions = (10, 5)
    area = calculate_area(shape_type, dimensions)
    if area is not None:
        print(f"Shape: {shape_type}")
        print(f"Dimensions: {dimensions}")
        print(f"Area: {area}")
    else:
        print("Invalid shape type specified.")