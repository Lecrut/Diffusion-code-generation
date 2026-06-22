import math

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calculate_area(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError('The given side lengths do not form a valid triangle.')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == '__main__':
    sides = [8, 15, 17]
    try:
        area = calculate_area(*sides)
        print(area)
    except ValueError as e:
        print(e)