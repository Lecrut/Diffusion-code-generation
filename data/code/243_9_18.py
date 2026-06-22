import math
PI = math.pi

def calculate_circle_circumference(radius):
    return 2 * PI * radius
if __name__ == '__main__':
    sample_radius = 3.14
    circumference = calculate_circle_circumference(sample_radius)
    print(circumference)