import math
def calculate_area(dimensions):
    n = len(dimensions)
    if n < 3:
        if n == 2:
            return 0.5 * dimensions[0] * dimensions[1]
        return 0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += dimensions[i][0] * dimensions[j][1]
        area -= dimensions[i][1] * dimensions[j][0]
    area = 0.5 * abs(area)
    return area
if __name__ == '__main__':
    rectangle_dims = [
        (0, 0),
        (4, 0),
        (4, 3),
        (0, 3)
    ]
    print(f"Rectangle Area: {calculate_area(rectangle_dims)}")
    triangle_dims = [
        (1, 1),
        (3, 4),
        (5, 2)
    ]
    print(f"Triangle Area: {calculate_area(triangle_dims)}")
    pentagon_dims = [
        (1, 1),
        (4, 0),
        (6, 2),
        (5, 5),
        (2, 4)
    ]
    print(f"Pentagon Area: {calculate_area(pentagon_dims)}")