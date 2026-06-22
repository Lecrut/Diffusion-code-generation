import math

def calculate_circumference(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 7
    circumference = calculate_circumference(sample_radius)
    print(f"Circumference for radius {sample_radius}: {circumference}")