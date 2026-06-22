import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def is_valid_triangle(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")
    return a + b > c and a + c > b and b + c > a

def triangle_sides_from_points(p1, p2, p3):
    side1 = calculate_distance(p1, p2)
    side2 = calculate_distance(p2, p3)
    side3 = calculate_distance(p3, p1)
    return [side1, side2, side3]

if __name__ == '__main__':
    try:
        point1 = (0, 0)
        point2 = (3, 4)
        point3 = (6, 0)

        sides = triangle_sides_from_points(point1, point2, point3)
        print(f"Sides of the triangle: {sides}")

        if is_valid_triangle(sides):
            print("The points form a valid triangle.")
        else:
            print("The points do not form a valid triangle.")

    except ValueError as e:
        print(e)