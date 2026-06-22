import math

def circle_perimeter(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 10.5
    calc_perimeter = circle_perimeter(sample_radius)
    print(f"Circumference of the circle with radius {sample_radius}: {calc_perimeter:.2f}")