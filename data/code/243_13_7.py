import math

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius
if __name__ == '__main__':
    sample_radius = 10.5
    calculated_perimeter = calculate_circle_perimeter(sample_radius)
    print(f'The circumference of a circle with radius {sample_radius} is {calculated_perimeter:.2f}')