import math

def compute_circle_area(radius):
    squared_radius = radius * radius
    return math.pi * squared_radius

if __name__ == '__main__':
    test_radius = 12.5
    calculated_area = compute_circle_area(test_radius)
    print(calculated_area)