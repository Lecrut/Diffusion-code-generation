import math

def calculate_perimeter(radius):
    if radius > 0:
        perimeter = 2 * math.pi * radius
        return perimeter
    else:
        return 0

if __name__ == '__main__':
    sample_radius = 10
    perimeter = calculate_perimeter(sample_radius)
    print(perimeter)