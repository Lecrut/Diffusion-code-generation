import math

def compute_triangle_area(base, height):
    if base <= 0 or height <= 0:
        return 0.0
    return 0.5 * base * height

if __name__ == '__main__':
    base = 10
    height = 5
    area = compute_triangle_area(base, height)
    print(area)