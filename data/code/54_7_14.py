import math

def validate_radius(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def calculate_area(radius):
    validate_radius(radius)
    return math.pi * (radius ** 2)

def areas_of_circles(radii):
    area_dict = {}
    for radius in radii:
        try:
            area_dict[radius] = calculate_area(radius)
        except ValueError as e:
            print(f"Error calculating area for radius {radius}: {e}")
    return area_dict

if __name__ == '__main__':
    sample_radii = [3.0, 4.5, -1.0, 7.2]
    areas = areas_of_circles(sample_radii)
    print(areas)