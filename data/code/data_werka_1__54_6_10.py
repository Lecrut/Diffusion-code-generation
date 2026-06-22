import math
RADIUS_TO_DIAMETER = 2

def circle_area(radius):
    return math.pi * radius ** 2
if __name__ == '__main__':
    sample_radius = 3
    print(circle_area(sample_radius))