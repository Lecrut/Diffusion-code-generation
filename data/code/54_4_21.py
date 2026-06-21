import math

def area_from_diameter(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number.")
    
    radius = calculate_radius(diameter)
    area = calculate_area(radius)
    return area

def calculate_radius(diameter):
    return diameter / 2

def calculate_area(radius):
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    try:
        sample_diameter = 15
        print(f"Area of a circle with diameter {sample_diameter}: {area_from_diameter(sample_diameter)}")
    except ValueError as e:
        print(f"Error: {e}")