import math

def calculate_areas():
    areas = {
        'circle': math.pi * 5**2,
        'square': 4**2
    }
    total_area = sum(areas.values())
    return total_area

if __name__ == '__main__':
    print(calculate_areas())