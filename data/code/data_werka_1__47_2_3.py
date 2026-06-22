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
    try:
        a = 5
        b = 12
        c = 13
        area = calculate_area(a, b, c)
        print(area)
    except ValueError as e:
        print(e)