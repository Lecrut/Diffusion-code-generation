import math

def get_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius1 = 5.0
    area1 = get_area(sample_radius1)
    print(f"Area of circle with radius {sample_radius1}: {area1}")
    
    sample_radius2 = 7.25
    area2 = get_area(sample_radius2)
    print(f"Area of circle with radius {sample_radius2}: {area2}")