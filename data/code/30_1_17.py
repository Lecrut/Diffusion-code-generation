import math

def compute_circle_area(radius):
    return float(math.pi * radius ** 2)

if __name__ == '__main__':
    sample_radii = [1.0, 2.5, 5.0, 10.0]
    for r in sample_radii:
        area = compute_circle_area(r)
        print(area)