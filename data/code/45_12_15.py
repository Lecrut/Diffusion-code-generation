import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius1 = 7.0
    area1 = calculate_circle_area(sample_radius1)
    print(f"Area of circle with radius {sample_radius1}: {area1}")

    sample_radius2 = 3.5
    area2 = calculate_circle_area(sample_radius2)
    print(f"Area of circle with radius {sample_radius2}: {area2}")