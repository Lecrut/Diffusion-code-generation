import math

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_values = {'radius': 5}
    try:
        perimeter = calculate_circle_perimeter(sample_values['radius'])
        print(f"Perimeter of the circle with radius {sample_values['radius']}: {perimeter}")
    except KeyError as e:
        print(f"Missing key in sample values: {e}")