import math

def calculate_area_with_heron(side_lengths):
    if len(side_lengths) != 3:
        raise ValueError('Exactly three side lengths are required for a triangle.')
    a, b, c = side_lengths
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Side lengths must be positive numbers.')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given side lengths do not form a valid triangle.')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    try:
        side_lengths = [3, 4, 5]
        area = calculate_area_with_heron(side_lengths)
        print(area)
    except ValueError as e:
        print(e)