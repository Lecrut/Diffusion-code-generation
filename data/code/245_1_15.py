import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_square_area(length):
    return length * length

def check_areas_equal(circle_radius, square_length):
    circle_area = calculate_circle_area(circle_radius)
    square_area = calculate_square_area(square_length)
    return math.isclose(circle_area, square_area, rel_tol=1e-09)
if __name__ == '__main__':
    radius1 = 6.0
    length1 = 28.274333882308138
    print(f'Radius: {radius1}, Length: {length1}, Areas Equal: {check_areas_equal(radius1, length1)}')
    radius2 = 3.5
    length2 = 24.5
    print(f'Radius: {radius2}, Length: {length2}, Areas Equal: {check_areas_equal(radius2, length2)}')