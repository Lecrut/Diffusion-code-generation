import math
PI = math.pi

def calculate_radius(diameter):
    return diameter / 2

def area_from_diameter(diameter):
    if diameter <= 0:
        raise ValueError('Diameter must be a positive number.')
    radius = calculate_radius(diameter)
    area = PI * radius ** 2
    return area
if __name__ == '__main__':
    sample_diameters = [15, 30, 45]
    for diameter in sample_diameters:
        try:
            print(f'Area of a circle with diameter {diameter}: {area_from_diameter(diameter)}')
        except ValueError as e:
            print(f'Error: {e}')