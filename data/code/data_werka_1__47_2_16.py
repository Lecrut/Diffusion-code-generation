import math

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calculate_area(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError('The given side lengths do not form a valid triangle.')
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

if __name__ == '__main__':
    try:
        a = 6
        b = 8
        c = 10
        area = calculate_area(a, b, c)
        print(area)
    except ValueError as e:
        print(e)