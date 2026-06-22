import math

def compute_circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

if __name__ == '__main__':
    sample_radius = 7.5
    calculated_circumference = compute_circle_circumference(sample_radius)
    print(calculated_circumference)