import math
def calculate_rectangle_diagonal(length, width):
    return math.sqrt(length**2 + width**2)
def calculate_circle_radius(diameter):
    return diameter / 2
if __name__ == '__main__':
    rectangle_length = 3
    rectangle_width = 4
    circle_diameter = 10
    diagonal = calculate_rectangle_diagonal(rectangle_length, rectangle_width)
    radius = calculate_circle_radius(circle_diameter)
    if radius != 0:
        ratio = diagonal / radius
        print(ratio)
    else:
        print("Undefined ratio (division by zero)")