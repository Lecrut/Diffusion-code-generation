import math

def compute_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

if __name__ == '__main__':
    sample_radius = 5.0
    calculated_circumference = compute_circumference(sample_radius)
    print(calculated_circumference)