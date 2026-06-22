import math
PI_CONST = math.pi
SEMI_MAJOR_AXIS = 10.0
SEMI_MINOR_AXIS = 4.0
def calculate_ellipse_area(major, minor):
    return PI_CONST * major * minor
if __name__ == '__main__':
    result = calculate_ellipse_area(SEMI_MAJOR_AXIS, SEMI_MINOR_AXIS)
    print(result)