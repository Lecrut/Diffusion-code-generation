import math

def compute_area_difference(radius1, radius2):
    if radius1 < 0 or radius2 < 0:
        raise ValueError("Radii must be non-negative")
    
    def circle_area(radius):
        return math.pi * (radius ** 2)
    
    area1 = circle_area(radius1)
    area2 = circle_area(radius2)
    return abs(area1 - area2)

if __name__ == '__main__':
    sample_values = {
        'circle1': {'radius': 5.0},
        'circle2': {'radius': 3.0}
    }
    
    radius1 = sample_values['circle1']['radius']
    radius2 = sample_values['circle2']['radius']
    
    difference = compute_area_difference(radius1, radius2)
    print(difference)