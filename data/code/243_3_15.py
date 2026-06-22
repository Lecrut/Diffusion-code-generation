import math

def calculate_circumference(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 15
    circumference = calculate_circumference(sample_radius)
    print(f"The circumference of a circle with radius {sample_radius} is {circumference:.2f}")