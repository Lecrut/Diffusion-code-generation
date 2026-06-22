import math

def compute_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 3.5
    calculated_area = compute_circle_area(sample_radius)
    print(f"The area of the circle with radius {sample_radius} is {calculated_area:.2f}")