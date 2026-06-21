import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

def calculate_areas(radii):
    areas = {}
    for radius in radii:
        validate_radius(radius)
        area = math.pi * (radius ** 2)
        areas[radius] = area
    return areas

if __name__ == '__main__':
    sample_radii = [1.0, 3.5, 6.2, -2.0, 'b']
    try:
        calculated_areas = calculate_areas(sample_radii)
        for radius, area in calculated_areas.items():
            print(f"Radius: {radius}, Area: {area:.2f}")
    except ValueError as e:
        print(e)