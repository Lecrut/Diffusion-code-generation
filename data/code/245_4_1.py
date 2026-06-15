import math
def calculate_area(shape, dim1, dim2=None):
    if shape == "circle":
        return math.pi * (dim1 ** 2)
    elif shape == "square":
        return dim1 * dim1
    else:
        raise ValueError("Unknown shape")
if __name__ == '__main__':
    circle_dim = 5
    square_dim = 5
    try:
        circle_area = calculate_area("circle", circle_dim)
        square_area = calculate_area("square", square_dim)
        if circle_area == square_area:
            print("The areas are equal.")
        else:
            print("The areas are not equal.")
    except ValueError as e:
        print(f"Error: {e}")