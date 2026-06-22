import math

def compute_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    default_radius = 5
    circle_area = compute_circle_area(default_radius)
    print(circle_area)