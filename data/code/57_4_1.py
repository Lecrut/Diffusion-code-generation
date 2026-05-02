import math
def calculate_area(shape, dimensions):
    if shape == "rectangle":
        return dimensions[0] * dimensions[1]
    elif shape == "circle":
        radius = dimensions[0]
        return math.pi * (radius ** 2)
    elif shape == "triangle":
        base = dimensions[0]
        height = dimensions[1]
        return 0.5 * base * height
    else:
        return None
if __name__ == '__main__':
    shape_type = "rectangle"
    dimensions = [10, 5]
    print(f"Shape: {shape_type}")
    print(f"Dimensions: {dimensions}")
    area = calculate_area(shape_type, dimensions)
    if area is not None:
        print(f"The area of the {shape_type} is: {area}")
    else:
        print("Invalid shape type specified.")