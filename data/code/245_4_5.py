import math
def calculate_area(shape, dim1, dim2=None):
    if shape == "circle":
        return math.pi * (dim1 ** 2)
    elif shape == "square":
        return dim1 * dim1
    else:
        raise ValueError("Unknown shape")
if __name__ == '__main__':
    shape1 = "circle"
    dim1_circle = 5.0
    shape2 = "square"
    dim1_square = 5.0
    try:
        area1 = calculate_area(shape1, dim1_circle)
        area2 = calculate_area(shape2, dim1_square)
        if area1 == area2:
            print("The areas are equal.")
        else:
            print("The areas are not equal.")
    except ValueError as e:
        print(f"Error: {e}")