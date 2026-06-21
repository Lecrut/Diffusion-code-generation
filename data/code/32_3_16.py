import math

VALID_TYPE = (int, float)
NON_NEGATIVE_THRESHOLD = 0

def get_rectangle_area(width, height):
    if not isinstance(width, VALID_TYPE) or isinstance(width, bool):
        raise TypeError("Width must be a number.")
    if not isinstance(height, VALID_TYPE) or isinstance(height, bool):
        raise TypeError("Height must be a number.")
    if width < NON_NEGATIVE_THRESHOLD or height < NON_NEGATIVE_THRESHOLD:
        raise ValueError("Dimensions cannot be negative.")
    return width * height

if __name__ == '__main__':
    DIM_W = 4
    DIM_H = 9
    computed = get_rectangle_area(DIM_W, DIM_H)
    print(computed)