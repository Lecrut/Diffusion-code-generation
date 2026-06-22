import math

def compute_ellipse_areas(pairs):
    if not isinstance(pairs, (list, tuple)):
        raise TypeError("pairs must be a list or tuple of tuples")
    
    results = []
    for pair in pairs:
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            raise ValueError("Each pair must be a tuple of two numbers")
        major, minor = pair
        if not isinstance(major, (int, float)) or not isinstance(minor, (int, float)):
            raise TypeError("Major and minor axes must be numbers")
        if major < 0 or minor < 0:
            raise ValueError("Major and minor axes must be non-negative")
        area = math.pi * major * minor
        results.append(area)
    
    return results

if __name__ == '__main__':
    sample_pairs = [(5.0, 3.0), (10, 4), (7.5, 2.5)]
    areas = compute_ellipse_areas(sample_pairs)
    print(areas)