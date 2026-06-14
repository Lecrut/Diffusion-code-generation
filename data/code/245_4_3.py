import math
def calculate_area(shape, dim1, dim2=None):
    if shape == "circle":
        return math.pi * (dim1 ** 2)
    elif shape == "square":
        return dim1 * dim1
    else:
        raise ValueError("Unknown shape")
if __name__ == '__main__':
    circle_side = 5.0
    square_side = 5.0
    try:
        circle_area = calculate_area("circle", circle_side)
        square_area = calculate_area("square", square_side)
        if circle_area == square_area:
            print("The areas are equal.")
        else:
            print("The areas are not equal.")
    except ValueError as e:
        print(f"Error: {e}")