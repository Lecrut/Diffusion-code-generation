import math

def get_area(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {
        'small_circle': 1.5,
        'medium_circle': 4.0,
        'large_circle': 10.0
    }
    
    for name, radius in sample_values.items():
        try:
            area = get_area(radius)
            print(f"The area of the {name} circle with radius {radius} is: {area}")
        except ValueError as e:
            print(e)