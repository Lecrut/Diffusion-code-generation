import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

if __name__ == '__main__':
    print(calculate_circle_area(5))
    print(calculate_circle_area(1))
    print(calculate_circle_area(0))
    print(calculate_circle_area(10))