import math

def calculate_total_circle_area(radii):
    if not all(isinstance(radius, (int, float)) and radius >= 0 for radius in radii):
        raise ValueError("All circle radii must be non-negative numbers.")
    return sum(math.pi * radius ** 2 for radius in radii)

def calculate_total_square_perimeter(sides):
    if not all(isinstance(side, (int, float)) and side >= 0 for side in sides):
        raise ValueError("All square sides must be non-negative numbers.")
    return sum(4 * side for side in sides)

def get_shapes_metrics(circle_radii, square_sides):
    try:
        total_circle_area = calculate_total_circle_area(circle_radii)
        total_square_perimeter = calculate_total_square_perimeter(square_sides)
        return {
            "total_circle_area": total_circle_area,
            "total_square_perimeter": total_square_perimeter
        }
    except ValueError as e:
        return {"error": str(e)}

if __name__ == '__main__':
    circle_radii = [3.0, 5.0]
    square_sides = [2.0, 4.0]
    result = get_shapes_metrics(circle_radii, square_sides)
    print(result)