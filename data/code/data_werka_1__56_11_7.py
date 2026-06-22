import math

def calculate_areas_and_perimeters(circle_radii, square_sides):
    total_circle_area = sum(math.pi * r**2 for r in circle_radii)
    total_square_perimeter = sum(4 * s for s in square_sides)
    return {
        'total_circle_area': total_circle_area,
        'total_square_perimeter': total_square_perimeter
    }

if __name__ == '__main__':
    circle_radii = [3, 5]
    square_sides = [4, 6]
    result = calculate_areas_and_perimeters(circle_radii, square_sides)
    print(result)