import math

def compute_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 3.0
    print(compute_area(sample_radius))