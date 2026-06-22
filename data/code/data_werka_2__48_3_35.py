import math

def calculate_triangle_area(sides):
    if len(sides) != 3:
        raise ValueError('Exactly three side lengths are required.')
    a, b, c = sides
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('Invalid side lengths: do not satisfy triangle inequality theorem.')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    try:
        sides = [3, 4, 5]
        area = calculate_triangle_area(sides)
        print(area)
    except ValueError as e:
        print(e)