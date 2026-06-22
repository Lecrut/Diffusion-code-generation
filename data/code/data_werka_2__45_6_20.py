import math
PI = math.pi

def compute_circle_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radii = [3, 7, 0.5, 15]
    for radius in sample_radii:
        area = compute_circle_area(radius)
        print(f'Area of circle with radius {radius}: {area}')