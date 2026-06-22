import math

def compute_area_difference(radius1, radius2):
    if radius1 < 0 or radius2 < 0:
        raise ValueError("Radii must be non-negative")
    return abs(math.pi * (radius1 ** 2) - math.pi * (radius2 ** 2))

if __name__ == '__main__':
    sample_radius1 = 10
    sample_radius2 = 4
    area_difference = compute_area_difference(sample_radius1, sample_radius2)
    print(area_difference)