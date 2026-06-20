import math

def calculate_area(sides):
    if not isinstance(sides, list):
        raise TypeError("Input must be a list of side lengths.")
    if len(sides) != 3:
        raise ValueError("Exactly three side lengths are required to form a triangle.")
    for side in sides:
        if not isinstance(side, (int, float)):
            raise TypeError("All side lengths must be numeric.")
        if side <= 0:
            raise ValueError("Side lengths must be positive.")
    a, b, c = sides
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("The given side lengths do not form a valid triangle.")
    s = (a + b + c) / 2
    area_squared = s * (s - a) * (s - b) * (s - c)
    if area_squared < 0:
        raise ValueError("The given side lengths do not form a valid triangle.")
    return math.sqrt(area_squared)

if __name__ == '__main__':
    sides = [3, 4, 5]
    area = calculate_area(sides)
    print(area)