import math
PI = math.pi

def calculate_circle_perimeter(radius):
    return 2 * PI * radius
if __name__ == '__main__':
    sample_radius = 5
    print(calculate_circle_perimeter(sample_radius))