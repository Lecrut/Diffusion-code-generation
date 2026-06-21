import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_square_perimeter(side_length):
    return 4 * side_length

def calculate_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2):
    total_circle_area = calculate_circle_area(circle_radius1) + calculate_circle_area(circle_radius2)
    total_square_perimeter = calculate_square_perimeter(square_side1) + calculate_square_perimeter(square_side2)
    return {
        'total_circle_area': total_circle_area,
        'total_square_perimeter': total_square_perimeter
    }

if __name__ == '__main__':
    circle_radius1 = 2
    circle_radius2 = 4
    square_side1 = 5
    square_side2 = 7
    result = calculate_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2)
    print(result)