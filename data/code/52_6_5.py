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
    area = 0.5 * abs(area)
    return area
if __name__ == '__main__':
    triangle_sides = [(3, 4, 5)]
    print(f"Triangle Area: {calculate_area(triangle_sides)}")
    quad_sides = [
        (0, 0),
        (4, 0),
        (4, 3),
        (0, 3)
    ]
    print(f"Quadrilateral Area: {calculate_area(quad_sides)}")
    pentagon_sides = [
        (1, 1),
        (3, 0),
        (4, 2),
        (2, 4),
        (0, 3)
    ]
    print(f"Pentagon Area: {calculate_area(pentagon_sides)}")
    line = [(1, 0), (5, 0)]
    print(f"Line Area: {calculate_area(line)}")
    square_sides = [
        (0, 0),
        (2, 0),
        (2, 2),
        (0, 2)
    ]
    print(f"Square Area: {calculate_area(square_sides)}")