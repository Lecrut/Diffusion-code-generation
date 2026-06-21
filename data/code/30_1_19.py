import math

def compute_circle_area(radius):
    return float(math.pi * radius * radius)

if __name__ == '__main__':
    sample_radii = [0, 1, 2.5, 10, 100]
    for r in sample_radii:
        area = compute_circle_area(r)
        print(f"Radius: {r}, Area: {area}")