import math

def compute_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    default_radius = 5.0
    calculated_area = compute_circle_area(default_radius)
    print(calculated_area)