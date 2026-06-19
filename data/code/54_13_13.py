import math

def compute_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    test_radius = 3.0
    calculated_area = compute_area(test_radius)
    print(f"The area of a circle with radius {test_radius} is: {calculated_area}")