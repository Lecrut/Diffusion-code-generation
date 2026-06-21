import math
PI = math.pi

def calculate_circle_area(diameter):
    if diameter <= 0:
        raise ValueError('Diameter must be positive')
    radius = diameter / 2
    area = PI * radius ** 2
    return area
if __name__ == '__main__':
    sample_diameters = [8, 12, -5, 0]
    for diameter in sample_diameters:
        try:
            print(f'Area of circle with diameter {diameter}: {calculate_circle_area(diameter)}')
        except ValueError as e:
            print(f'Error for diameter {diameter}: {e}')