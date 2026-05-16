import math
def calculate_shapes(radius, side):
    circumference = 2 * math.pi * radius
    perimeter = 4 * side
    return (circumference, perimeter)
if __name__ == '__main__':
    circle_radius = 5.0
    square_side = 4.0
    results = calculate_shapes(circle_radius, square_side)
    print(results)