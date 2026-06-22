import math
MIN_SIDE_LENGTH = 0.1

def is_valid_triangle(a, b, c):
    return a > MIN_SIDE_LENGTH and b > MIN_SIDE_LENGTH and (c > MIN_SIDE_LENGTH)

def calculate_perimeter(s1, s2, s3):
    if not is_valid_triangle(*sorted([s1, s2, s3])):
        raise ValueError('Invalid triangle sides')
    s = (s1 + s2 + s3) / 2
    return math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
if __name__ == '__main__':
    try:
        print(calculate_perimeter(3, 4, 5))
    except ValueError as e:
        print(e)