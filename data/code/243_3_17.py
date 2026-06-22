import math
PI = math.pi

def calculate_circumference(radius):
    return 2 * PI * radius
if __name__ == '__main__':
    sample_radius = 10
    circumference = calculate_circumference(sample_radius)
    print(f'The circumference of a circle with radius {sample_radius} is {circumference:.2f}')