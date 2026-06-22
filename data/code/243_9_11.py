import math

def compute_circumference(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 3.14
    calculated_circumference = compute_circumference(sample_radius)
    print(f"The circumference of a circle with radius {sample_radius} is {calculated_circumference:.2f}")