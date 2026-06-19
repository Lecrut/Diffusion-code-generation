import math

def compute_area(radius):
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 3.5
    area_result = compute_area(sample_radius)
    print(f"The area of the circle with radius {sample_radius} is {area_result:.2f}")