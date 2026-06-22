import math

def validate_input(sides, circumradius, radius):
    if sides < 3:
        raise ValueError("Number of sides must be at least 3")
    if circumradius <= 0:
        raise ValueError("Circumradius must be greater than 0")
    if radius <= 0:
        raise ValueError("Radius must be greater than 0")

def polygon_area(sides, circumradius):
    validate_input(sides, circumradius, None)
    return (sides * (circumradius ** 2)) / (4 * math.tan(math.pi / sides))

def circle_area(radius):
    validate_input(None, None, radius)
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_sides = 6
    sample_circumradius = 5
    sample_radius = 3
    polygon_areas = [polygon_area(s, sample_circumradius) for s in range(3, sample_sides + 1)]
    circle_areas = [circle_area(sample_radius)]
    print("Polygon areas:", polygon_areas)
    print("Circle area:", circle_areas)