import math

def is_valid_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

def calculate_triangle_area(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError('The given side lengths do not form a valid triangle')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == '__main__':
    try:
        side1 = 7
        side2 = 8
        side3 = 9
        area = calculate_triangle_area(side1, side2, side3)
        print(f'The area of the triangle with sides {side1}, {side2}, and {side3} is: {area}')
    except ValueError as e:
        print(e)