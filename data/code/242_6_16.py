import math
TRAPEZOID_BASE1 = 6
TRAPEZOID_BASE2 = 8
TRAPEZOID_HEIGHT = 4
CIRCLE_DIAMETER = 5

def calculate_trapezoid_area(base1, base2, height):
    return (base1 + base2) / 2 * height

def calculate_circle_area(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2

def compare_areas(trapezoid_base1, trapezoid_base2, trapezoid_height, circle_diameter):
    trapezoid_area = calculate_trapezoid_area(trapezoid_base1, trapezoid_base2, trapezoid_height)
    circle_area = calculate_circle_area(circle_diameter)
    if trapezoid_area > circle_area:
        return 'Trapezoid area is larger'
    elif trapezoid_area < circle_area:
        return 'Circle area is larger'
    else:
        return 'Areas are equal'
if __name__ == '__main__':
    comparison_result = compare_areas(TRAPEZOID_BASE1, TRAPEZOID_BASE2, TRAPEZOID_HEIGHT, CIRCLE_DIAMETER)
    print(f'Comparison result: {comparison_result}')