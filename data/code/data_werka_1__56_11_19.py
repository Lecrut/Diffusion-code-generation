import math

def calculate_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2):
    areas = {
        'circle1_area': math.pi * (circle_radius1 ** 2),
        'circle2_area': math.pi * (circle_radius2 ** 2)
    }
    
    perimeters = {
        'square1_perimeter': 4 * square_side1,
        'square2_perimeter': 4 * square_side2
    }
    
    return {'total_circle_area': sum(areas.values()), 'total_square_perimeter': sum(perimeters.values())}

if __name__ == '__main__':
    circle_radius1 = 5.0
    circle_radius2 = 3.0
    square_side1 = 4.0
    square_side2 = 6.0
    
    result = calculate_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2)
    
    print(result)