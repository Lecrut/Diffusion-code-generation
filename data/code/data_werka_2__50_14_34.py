import math

def compute_area_difference(radius1, radius2):
    if radius1 < 0 or radius2 < 0:
        raise ValueError("Radii must be non-negative")
    
    areas = {
        'circle1': math.pi * (radius1 ** 2),
        'circle2': math.pi * (radius2 ** 2)
    }
    
    return abs(areas['circle1'] - areas['circle2'])

if __name__ == '__main__':
    radius1 = 8.0
    radius2 = 4.5
    difference = compute_area_difference(radius1, radius2)
    print(difference)