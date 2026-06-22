import math

def polygon_area(sides, circumradius):
    return (sides * (circumradius ** 2)) / (4 * math.tan(math.pi / sides))

def circle_area(radius):
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_sides = 6
    sample_circumradius = 5
    sample_radius = 5

    poly_area = polygon_area(sample_sides, sample_circumradius)
    circ_area = circle_area(sample_radius)

    print(f"Polygon area: {poly_area}")
    print(f"Circle area: {circ_area}")
    print(f"Match: {math.isclose(poly_area, circ_area)}")