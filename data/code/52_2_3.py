import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {
        'radius1': 3,
        'radius2': 7.5,
        'radius3': 10
    }
    
    for name, radius in sample_values.items():
        area = calculate_circle_area(radius)
        print(f"The area of the circle with {name} radius {radius} is {area:.2f}")