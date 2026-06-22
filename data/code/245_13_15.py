import math

def polygon_area(sides, circumradius):
    return sides * (circumradius ** 2) * math.sin(2 * math.pi / sides) / 2

def circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_sides = 7
    sample_circumradius = 3.5
    sample_radius = 4.109861526062784
    polygon_calc_area = polygon_area(sample_sides, sample_circumradius)
    circle_calc_area = circle_area(sample_radius)
    print("Polygon area:", polygon_calc_area)
    print("Circle area:", circle_calc_area)