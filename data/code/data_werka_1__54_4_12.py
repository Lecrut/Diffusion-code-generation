import math

def area_from_diameter(diameter):
    if diameter > 0:
        radius = diameter / 2
        return math.pi * radius ** 2
    else:
        return None
if __name__ == '__main__':
    sample_values = {'diameter1': 10, 'diameter2': 5.5, 'diameter3': -3}
    for name, diameter in sample_values.items():
        area = area_from_diameter(diameter)
        print(f'Area of circle with {name} diameter {diameter}: {area}')