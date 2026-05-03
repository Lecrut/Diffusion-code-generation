def calculate_area(shape, dimensions):
    if shape == "rectangle":
        return dimensions[0] * dimensions[1]
    elif shape == "circle":
        import math
        return math.pi * (dimensions[0] ** 2)
    elif shape == "triangle":
        return 0.5 * dimensions[0] * dimensions[1]
    else:
        return None
if __name__ == '__main__':
    shape_type = "rectangle"
    dimensions = [10, 5]
    area = calculate_area(shape_type, dimensions)
    if area is not None:
        print(f"Shape: {shape_type}")
        print(f"Dimensions: {dimensions}")
        print(f"Area: {area}")
    else:
        print("Invalid shape type specified.")