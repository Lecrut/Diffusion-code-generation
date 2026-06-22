def kite_area(d1, d2):
    return 0.5 * d1 * d2

def circle_area(radius):
    import math
    return math.pi * radius ** 2

if __name__ == '__main__':
    shapes = {
        'kite': (4, 6),
        'circle': 5 / 2
    }
    
    total_area = kite_area(*shapes['kite']) + circle_area(shapes['circle'])
    print(total_area)