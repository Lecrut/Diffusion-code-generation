import math

def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

def calculate_heron_area(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError('The given side lengths do not form a valid triangle')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == '__main__':
    try:
        side_a = 7
        side_b = 10
        side_c = 5
        area = calculate_heron_area(side_a, side_b, side_c)
        print(f'The area of the triangle with sides {side_a}, {side_b}, and {side_c} is: {area}')
    except ValueError as e:
        print(e)