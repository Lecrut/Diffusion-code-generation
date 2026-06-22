import math

def calculate_circle_perimeter(radius):
    circumference = 2 * math.pi * radius
    return circumference

if __name__ == '__main__':
    sample_radius = 7.5
    perimeter = calculate_circle_perimeter(sample_radius)
    print(perimeter)