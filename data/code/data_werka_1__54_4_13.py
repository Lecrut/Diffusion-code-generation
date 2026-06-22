import math

def area_from_diameter(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number.")
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    try:
        sample_diameter = 10
        circle_area = area_from_diameter(sample_diameter)
        print(circle_area)
    except ValueError as e:
        print(f"Error: {e}")