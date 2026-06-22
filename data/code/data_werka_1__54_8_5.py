import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def calculate_circle_area(radius):
    validate_radius(radius)
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = [
        {'size': 'small', 'radius': 1},
        {'size': 'medium', 'radius': 5},
        {'size': 'large', 'radius': 10}
    ]
    
    for value in sample_values:
        try:
            area = calculate_circle_area(value['radius'])
            print(f"The area of a circle with {value['size']} radius ({value['radius']}) is: {area}")
        except (TypeError, ValueError) as e:
            print(e)