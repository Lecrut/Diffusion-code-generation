import math

def calculate_circle_circumference(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 10
    circumference = calculate_circle_circumference(sample_radius)
    print(circumference)