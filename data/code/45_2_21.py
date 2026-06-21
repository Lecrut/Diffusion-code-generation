import math

def calculate_circle_area(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be positive")
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    sample_diameters = [8.0, 12.5, -4.0, 0]
    for d in sample_diameters:
        try:
            circle_area = calculate_circle_area(d)
            print(f"Area of circle with diameter {d}: {circle_area}")
        except ValueError as e:
            print(f"Error for diameter {d}: {e}")