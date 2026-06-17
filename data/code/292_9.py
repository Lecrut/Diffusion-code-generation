import sys
def calculate_perimeter(shape_type, dimensions):
    if shape_type == "rectangle":
        length, width = dimensions
        return 2 * (length + width)
    elif shape_type == "square":
        side = dimensions[0]
        return 4 * side
    else:
        return 0
if __name__ == '__main__':
    shape_type = "rectangle"
    dimensions = [10, 5]
    perimeter = calculate_perimeter(shape_type, dimensions)
    print(perimeter)