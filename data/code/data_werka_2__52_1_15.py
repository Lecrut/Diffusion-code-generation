import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {
        'radius1': 3.0,
        'radius2': 7.5,
        'radius3': 10.0
    }
    
    for key, value in sample_values.items():
        area = calculate_circle_area(value)
        print(f"Area of circle with {key}: {area}")