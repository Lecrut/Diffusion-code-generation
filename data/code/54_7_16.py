import math

def calculate_circle_areas(radii):
    areas = {}
    for radius in radii:
        if not isinstance(radius, (int, float)) or radius < 0:
            raise ValueError(f"Invalid radius: {radius}. Radius must be a non-negative number.")
        area = math.pi * (radius ** 2)
        areas[radius] = area
    return areas

if __name__ == '__main__':
    sample_radii = [3, 5.5, 7, -1, 'a', 0]
    try:
        circle_areas = calculate_circle_areas(sample_radii)
        for radius, area in circle_areas.items():
            print(f"Radius: {radius}, Area: {area}")
    except ValueError as e:
        print(e)