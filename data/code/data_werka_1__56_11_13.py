import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

def calculate_square_area(side):
    return side ** 2

def calculate_square_perimeter(side):
    return 4 * side

def total_areas_and_perimeters(circle_radii, square_sides):
    total_circle_area = sum(calculate_circle_area(radius) for radius in circle_radii)
    total_square_perimeter = sum(calculate_square_perimeter(side) for side in square_sides)
    return {
        'total_circle_area': total_circle_area,
        'total_square_perimeter': total_square_perimeter
    }

if __name__ == '__main__':
    circle_radii = [3.0, 5.0]
    square_sides = [2.0, 4.0]
    result = total_areas_and_perimeters(circle_radii, square_sides)
    print(result)