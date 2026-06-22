import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {
        'radius1': 3.0,
        'radius2': 8.5,
        'radius3': 12.75
    }
    
    for name, radius in sample_values.items():
        area = calculate_circle_area(radius)
        print(f"Area of circle with {name} radius ({radius}): {area}")