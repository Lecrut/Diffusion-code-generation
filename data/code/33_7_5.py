import math

def calculate_triangle_area(base, height):
    return (base * height) / 2.0

if __name__ == '__main__':
    base = 10.0
    height = 5.0
    area = calculate_triangle_area(base, height)
    print(area)