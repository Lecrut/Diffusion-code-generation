import math

def validate_diameter(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number.")

def calculate_radius_from_diameter(diameter):
    return diameter / 2

def area_from_diameter(diameter):
    validate_diameter(diameter)
    radius = calculate_radius_from_diameter(diameter)
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    sample_diameters = [10, 25, 0, -5]
    for diameter in sample_diameters:
        try:
            area = area_from_diameter(diameter)
            print(f"The area of a circle with diameter {diameter} is {area}")
        except ValueError as e:
            print(f"Error: {e}")