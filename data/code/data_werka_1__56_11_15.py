import math

def calculate_total_circle_area(radius1, radius2):
    return math.pi * (radius1 ** 2) + math.pi * (radius2 ** 2)

def calculate_total_square_perimeter(side1, side2):
    return 4 * side1 + 4 * side2

def compute_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2):
    total_circle_area = calculate_total_circle_area(circle_radius1, circle_radius2)
    total_square_perimeter = calculate_total_square_perimeter(square_side1, square_side2)
    return {
        'total_circle_area': total_circle_area,
        'total_square_perimeter': total_square_perimeter
    }

if __name__ == '__main__':
    circle_radius1 = 3.0
    circle_radius2 = 4.5
    square_side1 = 2.0
    square_side2 = 5.0
    
    result = compute_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2)
    print(result)