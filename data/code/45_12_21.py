import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {
        'small_circle': 3.5,
        'medium_circle': 7.0,
        'large_circle': 14.0
    }
    
    for name, radius in sample_values.items():
        try:
            area = calculate_circle_area(radius)
            print(f"Area of {name}: {area}")
        except ValueError as e:
            print(e)