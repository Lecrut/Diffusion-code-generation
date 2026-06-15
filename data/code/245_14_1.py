import math
def calculate_circle_area(radius):
    return math.pi * radius**2
def calculate_square_area(side):
    return side * side
def calculate_triangle_area(base, height):
    return 0.5 * base * height
if __name__ == '__main__':
    circle_radius = 5.0
    square_side = 5.0
    circle_area = calculate_circle_area(circle_radius)
    square_area = calculate_square_area(square_side)
    print(f"Circle Area: {circle_area}")
    print(f"Square Area: {square_area}")
    if circle_area == square_area:
        print("The areas are equal.")
    else:
        print("The areas are not equal.")