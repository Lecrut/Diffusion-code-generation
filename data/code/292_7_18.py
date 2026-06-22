from math import pi
RAMANUJAN_FACTOR = 1 + 3 * (pi / 4 - 1) / (10 * pi)

def calculate_perimeter(a, b):
    return RAMANUJAN_FACTOR * (a + b)
if __name__ == '__main__':
    semi_major_axis = 5
    semi_minor_axis = 3
    perimeter = calculate_perimeter(semi_major_axis, semi_minor_axis)
    print(f'Perimeter of ellipse with semi-major axis {semi_major_axis} and semi-minor axis {semi_minor_axis}: {perimeter}')