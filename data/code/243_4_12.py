import math

def calculate_circumference(radius):
    return 2 * radius * math.pi

if __name__ == '__main__':
    sample_radius = 5.0
    circumference = calculate_circumference(sample_radius)
    print(circumference)