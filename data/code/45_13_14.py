import math

def compute_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    circle_properties = {
        'radius': 5.0,
        'area': None
    }
    
    circle_properties['area'] = compute_circle_area(circle_properties['radius'])
    print(circle_properties['area'])