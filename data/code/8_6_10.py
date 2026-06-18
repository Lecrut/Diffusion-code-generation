import math

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle given its radius using math.pi."""
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_radii = [0.5, 10, 3.14]

    for r in sample_radii:
        area = calculate_circle_area(r)
        print(f"Radius: {r}, Area: {area:.6f}")