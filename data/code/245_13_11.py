import math

def polygon_area(n, R):
    return 0.5 * n * R**2 * math.sin(2 * math.pi / n)

def circle_area(r):
    return math.pi * r**2

if __name__ == '__main__':
    sides = 6
    circumradius = 10
    sample_circle_radius = 8

    poly_area = polygon_area(sides, circumradius)
    circ_area = circle_area(sample_circle_radius)

    print("Polygon area:", poly_area)
    print("Circle area:", circ_area)