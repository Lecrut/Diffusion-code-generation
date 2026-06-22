import math

def compute_circle_area(radius):
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    radius_value = 3
    area_of_circle = compute_circle_area(radius_value)
    print(area_of_circle)