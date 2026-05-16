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
    shape1 = "square"
    dims1 = 5
    area1 = area_calculator(shape1, dims1)
    print(f"Area of {shape1} with dimension {dims1}: {area1}")
    shape2 = "rectangle"
    dims2 = (4, 6)
    area2 = area_calculator(shape2, dims2)
    print(f"Area of {shape2} with dimensions {dims2}: {area2}")
    shape3 = "circle"
    dims3 = 3
    area3 = area_calculator(shape3, dims3)
    print(f"Area of {shape3} with radius {dims3}: {area3}")