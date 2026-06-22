import math

def area_from_diameter(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number.")
    
    radius = calculate_radius(diameter)
    return calculate_area(radius)

def calculate_radius(diameter):
    return diameter / 2

def calculate_area(radius):
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_diameters = [10, 25, 50]
    for diameter in sample_diameters:
        try:
            print(f"Area of a circle with diameter {diameter}: {area_from_diameter(diameter)}")
        except ValueError as e:
            print(f"Error: {e}")