import math

def area_from_diameter(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number.")
    
    def calculate_radius(d):
        return d / 2
    
    radius = calculate_radius(diameter)
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    try:
        sample_diameters = [10, -5, 0]
        for diameter in sample_diameters:
            print(f"Diameter: {diameter}, Area: {area_from_diameter(diameter)}")
    except ValueError as e:
        print(f"Error: {e}")