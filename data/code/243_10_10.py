import math

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 3.14
    perimeter = calculate_circle_perimeter(sample_radius)
    print(perimeter)