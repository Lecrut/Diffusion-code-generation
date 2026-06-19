import math

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calculate_area(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError('The given side lengths do not form a valid triangle.')
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

if __name__ == '__main__':
    sides = {
        'side_a': 7,
        'side_b': 10,
        'side_c': 5
    }
    try:
        area = calculate_area(sides['side_a'], sides['side_b'], sides['side_c'])
        print(area)
    except ValueError as e:
        print(e)