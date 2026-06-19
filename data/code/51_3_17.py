import math

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_values = {'circle1': {'radius': 4}, 'circle2': {'radius': 6}}
    for circle_name, details in sample_values.items():
        perimeter = calculate_circle_perimeter(details['radius'])
        print(f"The perimeter of {circle_name} is: {perimeter}")