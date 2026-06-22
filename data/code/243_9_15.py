import math

def calculate_circle_circumference(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 3.14
    circumference = calculate_circle_circumference(sample_radius)
    print(f"The circumference of a circle with radius {sample_radius} is {circumference:.2f}")