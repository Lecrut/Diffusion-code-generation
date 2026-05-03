import math
def area_calculator(shape_type, dimensions):
    if shape_type == "square":
        side = dimensions
        return side * side
    elif shape_type == "rectangle":
        length = dimensions[0]
        width = dimensions[1]
        return length * width
    elif shape_type == "circle":
        radius = dimensions
        return math.pi * (radius ** 2)
    else:
        return None
if __name__ == '__main__':
    shape_type_1 = "square"
    dimensions_1 = 5
    area_1 = area_calculator(shape_type_1, dimensions_1)
    print(f"Area of {shape_type_1} with dimension {dimensions_1}: {area_1}")
    shape_type_2 = "rectangle"
    dimensions_2 = (4, 6)
    area_2 = area_calculator(shape_type_2, dimensions_2)
    print(f"Area of {shape_type_2} with dimensions {dimensions_2}: {area_2}")
    shape_type_3 = "circle"
    dimensions_3 = 3
    area_3 = area_calculator(shape_type_3, dimensions_3)
    print(f"Area of {shape_type_3} with radius {dimensions_3}: {area_3}")