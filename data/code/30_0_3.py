import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius_positive = 5
    sample_radius_negative = -3
    
    try:
        area_positive = calculate_circle_area(sample_radius_positive)
        print(area_positive)
    except ValueError as e:
        print(e)
    
    try:
        area_negative = calculate_circle_area(sample_radius_negative)
        print(area_negative)
    except ValueError as e:
        print(e)