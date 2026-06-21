import math

def compute_circle_area(radius):
    return math.pi * radius * radius

if __name__ == '__main__':
    sample_radius = 5.0
    result = compute_circle_area(sample_radius)
    print(result)