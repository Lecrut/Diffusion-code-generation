import math

def calculate_perimeter(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 10
    perimeter = calculate_perimeter(sample_radius)
    print(f"Perimeter: {perimeter}")