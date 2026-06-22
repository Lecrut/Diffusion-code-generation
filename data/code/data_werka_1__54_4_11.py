import math

def validate_diameter(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number.")
    return True

def calculate_radius(diameter):
    return diameter / 2.0

def area_from_diameter(diameter):
    try:
        validate_diameter(diameter)
        radius = calculate_radius(diameter)
        area = math.pi * (radius ** 2)
        return area
    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_diameter = 10.0
    area = area_from_diameter(sample_diameter)
    if area is not None:
        print(area)