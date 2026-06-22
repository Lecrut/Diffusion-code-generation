import math

def calculate_circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

if __name__ == '__main__':
    sample_radius = 5.0
    calculated_circumference = calculate_circle_circumference(sample_radius)
    print(calculated_circumference)