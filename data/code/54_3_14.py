import math

def calculate_area(radius: float) -> float:
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radii = {
        'small': 0.5,
        'medium': 5.0,
        'large': 10.5
    }
    
    for name, radius in sample_radii.items():
        area = calculate_area(radius)
        print(f"The area of the {name} circle with radius {radius} is {area}")