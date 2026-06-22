import math

def calculate_ellipse_area(major_axis: float, minor_axis: float) -> float:
    if major_axis <= 0 or minor_axis <= 0:
        raise ValueError("Axis lengths must be positive")
    return math.pi * (major_axis / 2) * (minor_axis / 2)

def process_ellipse_pairs(pairs: list[tuple[float, float]]) -> list[float]:
    results = []
    for major, minor in pairs:
        if not isinstance(major, (int, float)) or not isinstance(minor, (int, float)):
            raise TypeError("Axis values must be numbers")
        area = calculate_ellipse_area(float(major), float(minor))
        results.append(area)
    return results

if __name__ == '__main__':
    sample_data = [
        (10, 5),
        (8, 4),
        (20, 15),
        (6, 2)
    ]
    computed_areas = process_ellipse_pairs(sample_data)
    for area in computed_areas:
        print(area)