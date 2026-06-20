import math

def calculate_circle_area(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be positive")
    radius = diameter / 2
    return math.pi * radius * radius

if __name__ == '__main__':
    sample_diameter = 10
    area = calculate_circle_area(sample_diameter)
    print(area)
    sample_diameter_2 = -5
    try:
        calculate_circle_area(sample_diameter_2)
    except ValueError as e:
        print(e)