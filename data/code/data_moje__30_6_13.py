import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a numeric value")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radii = [5, 3.5, 0, 10]
    for r in sample_radii:
        area = calculate_circle_area(r)
        print(area)
    
    try:
        calculate_circle_area("five")
    except TypeError as e:
        print(e)