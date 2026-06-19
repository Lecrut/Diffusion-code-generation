import math

def calculate_total_area_and_perimeter(circle_radii, square_sides):
    total_circle_area = sum(math.pi * (radius ** 2) for radius in circle_radii)
    total_square_perimeter = sum(4 * side for side in square_sides)
    return {
        "total_circle_area": total_circle_area,
        "total_square_perimeter": total_square_perimeter
    }

if __name__ == '__main__':
    circle_radii = [3.0, 5.0]
    square_sides = [4.0, 6.0]
    result = calculate_total_area_and_perimeter(circle_radii, square_sides)
    print(result)