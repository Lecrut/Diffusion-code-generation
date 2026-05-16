import math
def calculate_shapes(radius, side):
    circle_area = math.pi * (radius ** 2)
    circle_perimeter = 2 * math.pi * radius
    square_area = side ** 2
    square_perimeter = 4 * side
    return circle_area, circle_perimeter, square_area, square_perimeter
if __name__ == '__main__':
    circle_radius = 5.0
    square_side = 4.0
    circle_area, circle_perimeter, square_area, square_perimeter = calculate_shapes(circle_radius, square_side)
    print(f"Circle Area: {circle_area}")
    print(f"Circle Perimeter (Circumference): {circle_perimeter}")
    print(f"Square Area: {square_area}")
    print(f"Square Perimeter: {square_perimeter}")