import math

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 8
    computed_perimeter = calculate_circle_perimeter(sample_radius)
    print(f"The perimeter of a circle with radius {sample_radius} is {computed_perimeter:.2f}")