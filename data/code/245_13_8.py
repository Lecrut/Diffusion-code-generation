import math

def validate_input(sides, circumradius, radius):
    if sides < 3 or circumradius <= 0 or radius <= 0:
        raise ValueError("Invalid input values. Sides must be >= 3, circumradius and radius must be > 0.")

def polygon_area(sides, circumradius):
    return (sides * (circumradius ** 2)) / (4 * math.tan(math.pi / sides))

def circle_area(radius):
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_sides = 6
    sample_circumradius = 5
    sample_radius = 3

    validate_input(sample_sides, sample_circumradius, sample_radius)
    
    polygon_area_result = polygon_area(sample_sides, sample_circumradius)
    circle_area_result = circle_area(sample_radius)
    
    print(f"Polygon area: {polygon_area_result}")
    print(f"Circle area: {circle_area_result}")