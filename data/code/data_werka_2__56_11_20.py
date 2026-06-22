import math
PI = math.pi

def calculate_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2):

    def circle_area(radius):
        return PI * radius ** 2

    def square_perimeter(side_length):
        return 4 * side_length
    total_circle_area = circle_area(circle_radius1) + circle_area(circle_radius2)
    total_square_perimeter = square_perimeter(square_side1) + square_perimeter(square_side2)
    return {'total_circle_area': total_circle_area, 'total_square_perimeter': total_square_perimeter}
if __name__ == '__main__':
    circle_radius1 = 5.0
    circle_radius2 = 7.0
    square_side1 = 3.0
    square_side2 = 8.0
    result = calculate_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2)
    print(result)