import math
def calculate_area(shape, dimension1, dimension2):
    if shape == "rectangle":
        return dimension1 * dimension2
    elif shape == "circle":
        radius = dimension1
        return math.pi * (radius ** 2)
    elif shape == "triangle":
        return 0.5 * dimension1 * dimension2
    else:
        return None
if __name__ == '__main__':
    shape_type = "rectangle"
    dim1 = 10.0
    dim2 = 5.0
    area = calculate_area(shape_type, dim1, dim2)
    if area is not None:
        print(f"Shape: {shape_type}")
        print(f"Dimension 1: {dim1}")
        print(f"Dimension 2: {dim2}")
        print(f"Calculated Area: {area}")
    else:
        print("Invalid shape specified.")
    shape_type = "circle"
    dim1 = 7.0
    area = calculate_area(shape_type, dim1, None)
    if area is not None:
        print(f"\nShape: {shape_type}")
        print(f"Radius: {dim1}")
        print(f"Calculated Area: {area}")
    else:
        print("Invalid shape specified.")
    shape_type = "triangle"
    dim1 = 8.0
    dim2 = 6.0
    area = calculate_area(shape_type, dim1, dim2)
    if area is not None:
        print(f"\nShape: {shape_type}")
        print(f"Base: {dim1}")
        print(f"Height: {dim2}")
        print(f"Calculated Area: {area}")
    else:
        print("Invalid shape specified.")