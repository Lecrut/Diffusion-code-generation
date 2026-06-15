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
    triangle_base = 4.0
    triangle_height = 6.0
    circle_area = calculate_circle_area(circle_radius)
    square_area = calculate_square_area(square_side)
    triangle_area = calculate_triangle_area(triangle_base, triangle_height)
    print(f"Circle Area: {circle_area}")
    print(f"Square Area: {square_area}")
    print(f"Triangle Area: {triangle_area}")
    comparison_result = circle_area == square_area
    print(f"Are the circle and square areas equal? {comparison_result}")