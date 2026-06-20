import math

PI = math.pi

def circle_area(radius):
    return PI * radius * radius

if __name__ == '__main__':
    sample_radius = 5.0
    print(circle_area(sample_radius))
    sample_radius_2 = 10.0
    print(circle_area(sample_radius_2))