import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

if __name__ == '__main__':
    r1 = 5
    r2 = 10.5
    area1 = calculate_circle_area(r1)
    area2 = calculate_circle_area(r2)
    print(area1)
    print(area2)