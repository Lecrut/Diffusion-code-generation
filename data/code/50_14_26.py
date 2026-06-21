import math

def compute_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * (radius ** 2)

def compute_area_difference(radius1, radius2):
    area1 = compute_circle_area(radius1)
    area2 = compute_circle_area(radius2)
    return abs(area1 - area2)

if __name__ == '__main__':
    sample_values = {
        'circle1': {'radius': 8.0},
        'circle2': {'radius': 4.5}
    }
    
    radius1 = sample_values['circle1']['radius']
    radius2 = sample_values['circle2']['radius']
    
    area_difference = compute_area_difference(radius1, radius2)
    print(area_difference)