import math

def compute_area_difference(radius1, radius2):
    if radius1 < 0 or radius2 < 0:
        raise ValueError("Radii must be non-negative numbers.")
    
    area1 = math.pi * radius1 ** 2
    area2 = math.pi * radius2 ** 2
    
    return abs(area1 - area2)

if __name__ == '__main__':
    radius1 = 5.0
    radius2 = 3.0
    difference = compute_area_difference(radius1, radius2)
    print(difference)