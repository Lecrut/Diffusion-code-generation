import math

def is_valid_triangle(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        return False
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

if __name__ == '__main__':
    print(is_valid_triangle(3, 4, 5))
    print(is_valid_triangle(1, 2, 10))
    print(is_valid_triangle(-1, 4, 5))
    print(is_valid_triangle(0, 0, 0))