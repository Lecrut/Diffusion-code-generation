import math

def polygon_area(n, R):
    return (n * R**2) / (4 * math.tan(math.pi / n))

def circle_area(r):
    return math.pi * r**2

if __name__ == '__main__':
    sides = 6
    circumradius = 5
    sample_circle_radius = 7

    polygon_areas = [polygon_area(sides, circumradius) for _ in range(3)]
    circle_areas = [circle_area(sample_circle_radius) for _ in range(3)]

    print("Polygon areas:", polygon_areas)
    print("Circle areas:", circle_areas)