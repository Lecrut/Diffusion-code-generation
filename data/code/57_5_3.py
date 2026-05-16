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
    print(area_calculator("square", 5))
    print(area_calculator("rectangle", (4, 6)))
    print(area_calculator("circle", 3))