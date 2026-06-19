import math

def calculate_circle_area(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be positive")
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    try:
        sample_diameter1 = 5
        print(calculate_circle_area(sample_diameter1))
        
        sample_diameter2 = -3
        print(calculate_circle_area(sample_diameter2))
    except ValueError as e:
        print(e)