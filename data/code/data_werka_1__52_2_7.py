import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {
        'circle1': {'radius': 3},
        'circle2': {'radius': 7.5},
        'circle3': {'radius': 10}
    }
    
    for name, data in sample_values.items():
        radius = data['radius']
        area = calculate_circle_area(radius)
        print(f"The area of the {name} with radius {radius} is {area:.2f}")