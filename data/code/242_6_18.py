import math

def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def calculate_circle_area(diameter):
    radius = diameter / 2
    return math.pi * (radius ** 2)

def compare_areas(trapezoid_base1, trapezoid_base2, trapezoid_height, circle_diameter):
    trapezoid_area = calculate_trapezoid_area(trapezoid_base1, trapezoid_base2, trapezoid_height)
    circle_area = calculate_circle_area(circle_diameter)
    return trapezoid_area, circle_area

if __name__ == '__main__':
    base1 = 6
    base2 = 8
    height = 4
    diameter = 5
    trapezoid_area, circle_area = compare_areas(base1, base2, height, diameter)
    print(f"Trapezoid area: {trapezoid_area}")
    print(f"Circle area: {circle_area}")