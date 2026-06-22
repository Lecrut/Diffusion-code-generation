import math

CIRCLE_CIRCUMFERENCE_FACTOR = 2 * math.pi

def calculate_circumference(radius):
    return CIRCLE_CIRCUMFERENCE_FACTOR * radius

if __name__ == '__main__':
    sample_radius = 10
    circumference = calculate_circumference(sample_radius)
    print(f"The circumference of a circle with radius {sample_radius} is {circumference:.2f}")