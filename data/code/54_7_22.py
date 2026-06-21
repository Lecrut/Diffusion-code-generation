import math

def calculate_area(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)

def calculate_areas(radii):
    areas = {}
    for radius in radii:
        try:
            area = calculate_area(radius)
            areas[radius] = area
        except ValueError as e:
            print(f"Error processing radius {radius}: {e}")
    return areas

if __name__ == '__main__':
    sample_radii = [2.0, 3.5, -1.0, 'a', 4.8]
    calculated_areas = calculate_areas(sample_radii)
    for radius, area in calculated_areas.items():
        print(f"Radius: {radius}, Area: {area}")