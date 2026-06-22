import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_square_area(side_length):
    return side_length ** 2

def compare_areas(circle_radius, square_side_length):
    circle_area = calculate_circle_area(circle_radius)
    square_area = calculate_square_area(square_side_length)
    print(f"Circle area: {circle_area}")
    print(f"Square area: {square_area}")
    if circle_area > square_area:
        return "The circle has a larger area."
    elif circle_area < square_area:
        return "The square has a larger area."
    else:
        return "Both shapes have the same area."

if __name__ == '__main__':
    circle_radius = 5
    square_side_length = 6
    result = compare_areas(circle_radius, square_side_length)
    print(result)