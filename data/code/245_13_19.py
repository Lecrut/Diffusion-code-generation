import math

def polygon_area(sides, circumradius):
    return sides * (circumradius ** 2) * math.sin(2 * math.pi / sides) / 2

def circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_sides = 6
    sample_circumradius = 5
    sample_radius = 3.141592653589793
    polygon_areas = {s: polygon_area(s, sample_circumradius) for s in range(3, sample_sides + 1)}
    circle_areas = {r: circle_area(r) for r in [sample_radius]}
    print("Polygon areas:", polygon_areas)
    print("Circle area:", circle_areas)