import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

if __name__ == '__main__':
    r1 = 5
    r2 = 10.5
    print(calculate_circle_area(r1))
    print(calculate_circle_area(r2))