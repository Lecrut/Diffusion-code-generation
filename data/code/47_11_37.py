import math

def calculate_triangle_area(a, b, c):
    if not (a > 0 and b > 0 and (c > 0)):
        raise ValueError('Side lengths must be positive')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given side lengths do not form a valid triangle')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    try:
        side1 = 6
        side2 = 8
        side3 = 10
        triangle_area = calculate_triangle_area(side1, side2, side3)
        print(f'The area of the triangle with sides {side1}, {side2}, and {side3} is: {triangle_area}')
    except ValueError as e:
        print(e)