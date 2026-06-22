import math

def calculate_radius(diameter):
    return diameter / 2

def area_from_diameter(diameter):
    radius = calculate_radius(diameter)
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    sample_diameters = {
        'small': 10,
        'medium': 25,
        'large': 50
    }
    
    for size, diameter in sample_diameters.items():
        print(f"Area of a {size} circle with diameter {diameter}: {area_from_diameter(diameter)}")