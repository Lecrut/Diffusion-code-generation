import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius_1 = 7.0
    area_1 = calculate_circle_area(sample_radius_1)
    print(f"Area of circle with radius {sample_radius_1}: {area_1}")
    
    sample_radius_2 = 3.5
    area_2 = calculate_circle_area(sample_radius_2)
    print(f"Area of circle with radius {sample_radius_2}: {area_2}")