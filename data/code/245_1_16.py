import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_square_area(side_length):
    return side_length * side_length

def check_equal_areas(circle_radius, square_side_length):
    circle_area = calculate_circle_area(circle_radius)
    square_area = calculate_square_area(square_side_length)
    return math.isclose(circle_area, square_area, rel_tol=1e-09)
if __name__ == '__main__':
    r1 = 5.0
    l1 = 7.853981633974483
    print(f'Radius: {r1}, Side Length: {l1}, Areas Equal: {check_equal_areas(r1, l1)}')
    r2 = 3.0
    l2 = math.pi * 3.0
    print(f'Radius: {r2}, Side Length: {l2}, Areas Equal: {check_equal_areas(r2, l2)}')
    r3 = 1.0
    l3 = math.pi
    print(f'Radius: {r3}, Side Length: {l3}, Areas Equal: {check_equal_areas(r3, l3)}')