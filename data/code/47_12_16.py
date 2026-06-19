import math

def calculate_heron_area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Side lengths must be positive')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given sides do not form a valid triangle')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == '__main__':
    side_a = 7
    side_b = 8
    side_c = 9
    try:
        area = calculate_heron_area(side_a, side_b, side_c)
        print(area)
    except ValueError as e:
        print(e)