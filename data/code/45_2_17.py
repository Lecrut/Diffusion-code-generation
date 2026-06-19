import math

def calculate_circle_area(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be positive")
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    sample_diameters = [5, 10, -3, 0]
    for diameter in sample_diameters:
        try:
            area = calculate_circle_area(diameter)
            print(f"The area of a circle with diameter {diameter} is {area:.2f}")
        except ValueError as e:
            print(e)