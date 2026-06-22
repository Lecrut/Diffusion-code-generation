import math
from typing import List, Tuple

PI_CONSTANT = math.pi

def validate_axis_value(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Axis values must be numeric")
    if value < 0:
        raise ValueError("Axis values must be non-negative")
    return float(value)

def compute_single_area(major, minor):
    validated_major = validate_axis_value(major)
    validated_minor = validate_axis_value(minor)
    return PI_CONSTANT * validated_major * validated_minor

def compute_ellipse_areas(pairs: List[Tuple[float, float]]) -> List[float]:
    if not isinstance(pairs, list):
        raise TypeError("Input must be a list of pairs")
    
    areas = []
    for pair in pairs:
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            raise ValueError("Each pair must contain exactly two elements")
        
        major_axis, minor_axis = pair
        area = compute_single_area(major_axis, minor_axis)
        areas.append(area)
    
    return areas

if __name__ == '__main__':
    sample_pairs = [(5.0, 3.0), (10, 4), (7.5, 2.5)]
    results = compute_ellipse_areas(sample_pairs)
    for area in results:
        print(area)