import math

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_values = {
        'circle1': {'radius': 4},
        'circle2': {'radius': 9}
    }
    
    for circle_name, data in sample_values.items():
        perimeter = calculate_circle_perimeter(data['radius'])
        print(f"Perimeter of {circle_name}: {perimeter}")