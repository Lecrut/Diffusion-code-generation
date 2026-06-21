import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_square_perimeter(side_length):
    return 4 * side_length

def calculate_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2):
    circle_area1 = calculate_circle_area(circle_radius1)
    circle_area2 = calculate_circle_area(circle_radius2)
    total_circle_area = circle_area1 + circle_area2
    
    square_perimeter1 = calculate_square_perimeter(square_side1)
    square_perimeter2 = calculate_square_perimeter(square_side2)
    total_square_perimeter = square_perimeter1 + square_perimeter2
    
    return {'total_circle_area': total_circle_area, 'total_square_perimeter': total_square_perimeter}

if __name__ == '__main__':
    circle_radius1 = 5
    circle_radius2 = 8
    square_side1 = 7
    square_side2 = 9
    result = calculate_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2)
    print(result)