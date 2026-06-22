import math

def circle_area(radius):
    return math.pi * (radius ** 2)

def square_area(side_length):
    return side_length ** 2

def check_equal_areas(circle_radius, square_side_length):
    if circle_radius <= 0 or square_side_length <= 0:
        raise ValueError("Radii and side lengths must be positive.")
    return circle_area(circle_radius) == square_area(square_side_length)

if __name__ == '__main__':
    print(f"Equal Areas (5, 7): {check_equal_areas(5.0, 7.0)}")
    print(f"Equal Areas (3, pi*3): {check_equal_areas(3.0, math.pi * 3.0)}")
    print(f"Equal Areas (1, pi): {check_equal_areas(1.0, math.pi)}")