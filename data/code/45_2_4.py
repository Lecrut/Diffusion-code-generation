import math

def calculate_circle_area(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be positive")
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    sample_diameters = [7.5, 15.0, -2.0, 0]
    for diameter in sample_diameters:
        try:
            result_area = calculate_circle_area(diameter)
            print(f"Area of circle with diameter {diameter}: {result_area}")
        except ValueError as e:
            print(f"Error for diameter {diameter}: {e}")