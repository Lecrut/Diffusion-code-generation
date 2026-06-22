import math

def compute_circle_area(radius: float) -> float:
    return math.pi * radius * radius

if __name__ == "__main__":
    sample_radii = [1.0, 2.5, 10.0, 0.0]
    for r in sample_radii:
        result = compute_circle_area(r)
        print(result)