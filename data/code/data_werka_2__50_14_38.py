import math

def compute_area_difference(radius1, radius2):
    if radius1 < 0 or radius2 < 0:
        raise ValueError("Radii must be non-negative")
    
    area_1 = math.pi * (radius1 ** 2)
    area_2 = math.pi * (radius2 ** 2)
    
    difference = abs(area_1 - area_2)
    return difference

if __name__ == '__main__':
    sample_radius1 = 10
    sample_radius2 = 4
    result = compute_area_difference(sample_radius1, sample_radius2)
    print(result)