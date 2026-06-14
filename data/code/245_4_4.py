import math
def calculate_area(shape, dim1, dim2=None):
    if shape == "circle":
        return math.pi * (dim1 ** 2)
    elif shape == "square":
        return dim1 * dim1
    else:
        raise ValueError("Unknown shape")
if __name__ == '__main__':
    circle_dim = 5.0
    square_dim = 5.0
    shape1 = "circle"
    shape2 = "square"
    try:
        area1 = calculate_area(shape1, circle_dim)
        area2 = calculate_area(shape2, square_dim)
        if area1 == area2:
            print("The areas are equal.")
        else:
            print("The areas are not equal.")
    except ValueError as e:
        print(f"Error: {e}")