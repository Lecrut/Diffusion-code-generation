import math

def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def calculate_circle_area(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2

def compare_areas(trapezoid_bases, trapezoid_height, circle_diameter):
    trapezoid_area = calculate_trapezoid_area(*trapezoid_bases, trapezoid_height)
    circle_area = calculate_circle_area(circle_diameter)
    return trapezoid_area, circle_area

if __name__ == '__main__':
    trapezoid_b1 = 6
    trapezoid_b2 = 8
    trapezoid_h = 4
    circle_d = 5
    
    trapezoid_area, circle_area = compare_areas((trapezoid_b1, trapezoid_b2), trapezoid_h, circle_d)
    
    print(f"Trapezoid area: {trapezoid_area}")
    print(f"Circle area: {circle_area}")
    if trapezoid_area > circle_area:
        print("Trapezoid has a larger area.")
    elif trapezoid_area < circle_area:
        print("Circle has a larger area.")
    else:
        print("Areas are equal.")