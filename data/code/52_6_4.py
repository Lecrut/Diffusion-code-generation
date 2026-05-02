import math
def calculate_area(dimensions):
    n = len(dimensions)
    if n < 3:
        if n == 2:
            return 0
        elif n == 1:
            return 0
        else:
            return 0
    if n == 3:
        a, b, c = dimensions
        s = (a + b + c) / 2.0
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += dimensions[i][0] * dimensions[j][1]
        area -= dimensions[i][1] * dimensions[j][0]
    return abs(area) / 2.0
if __name__ == '__main__':
    triangle_sides = [(3, 4, 5)]
    print(f"Triangle Area: {calculate_area(triangle_sides)}")
    quadrilateral_coords = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(f"Quadrilateral Area: {calculate_area(quadrilateral_coords)}")
    pentagon_coords = [(1, 1), (4, 1), (5, 3), (3, 5), (0, 4)]
    print(f"Pentagon Area: {calculate_area(pentagon_coords)}")
    rectangle_coords = [(0, 0), (5, 0), (5, 2), (0, 2)]
    print(f"Rectangle Area: {calculate_area(rectangle_coords)}")