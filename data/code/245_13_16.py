import math

def polygon_area(sides, circumradius):
    return sides * (circumradius ** 2) * math.sin(2 * math.pi / sides) / 2

def circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_sides = 6
    sample_circumradius = 5
    sample_radius = 3.872983346207417
    polygon_result = polygon_area(sample_sides, sample_circumradius)
    circle_result = circle_area(sample_radius)
    print(f"Polygon area: {polygon_result}")
    print(f"Circle area: {circle_result}")