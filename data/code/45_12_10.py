import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radii = {'circle1': 5.0, 'circle2': 10.5}
    
    for name, radius in sample_radii.items():
        area = calculate_circle_area(radius)
        print(f"Area of {name}: {area}")