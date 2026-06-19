import math

def calculate_circle_area(radius):
    return math.pi * radius**2

if __name__ == '__main__':
    sample_values = {
        'radius1': 3.0,
        'radius2': 7.5,
        'radius3': 10.0
    }
    
    for key, value in sample_values.items():
        area = calculate_circle_area(value)
        print(f"The area of a circle with {key} radius {value} is {area}")