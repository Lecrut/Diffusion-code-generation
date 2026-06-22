import math

def compute_ellipse_areas(axis_pairs):
    if not isinstance(axis_pairs, (list, tuple)):
        raise TypeError("axis_pairs must be a list or tuple")
    
    areas = []
    for pair in axis_pairs:
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            raise ValueError("Each pair must contain exactly two numeric values")
        
        a, b = pair
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Axis values must be numeric")
        if a < 0 or b < 0:
            raise ValueError("Axis values must be non-negative")
            
        area = math.pi * a * b
        areas.append(area)
        
    return areas

if __name__ == '__main__':
    sample_pairs = [(5.0, 3.0), (10, 20), (7.5, 7.5)]
    results = compute_ellipse_areas(sample_pairs)
    print(results)