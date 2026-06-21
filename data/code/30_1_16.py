import math

def compute_circle_area(radius):
    return math.pi * radius * radius

if __name__ == '__main__':
    radius_1 = 5
    radius_2 = 10.5
    area_1 = compute_circle_area(radius_1)
    area_2 = compute_circle_area(radius_2)
    print(area_1)
    print(area_2)