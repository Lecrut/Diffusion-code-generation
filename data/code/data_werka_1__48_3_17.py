import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and (b + c > a)
if __name__ == '__main__':
    point1 = (0, 0)
    point2 = (3, 4)
    point3 = (6, 0)
    side1 = distance(*point1, *point2)
    side2 = distance(*point2, *point3)
    side3 = distance(*point3, *point1)
    print(f'Side 1: {side1}')
    print(f'Side 2: {side2}')
    print(f'Side 3: {side3}')
    triangle_result = is_triangle(side1, side2, side3)
    print(f'Is Triangle: {triangle_result}')