import math
def calculate_area(shape, dimension1, dimension2=None):
    if shape == "circle":
        radius = dimension1
        return math.pi * (radius ** 2)
    elif shape == "square":
        side = dimension1
        return side ** 2
    else:
        raise ValueError("Invalid shape specified")
if __name__ == '__main__':
    shape1 = "circle"
    dim1_val = 5.0
    shape2 = "square"
    dim2_val = 25.0
    try:
        area1 = calculate_area(shape1, dim1_val)
        area2 = calculate_area(shape2, dim2_val)
        if area1 == area2:
            print("The areas are equal.")
        else:
            print("The areas are not equal.")
    except ValueError as e:
        print(f"Error: {e}")