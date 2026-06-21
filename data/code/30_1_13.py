import math

def compute_circle_area(radius):
    return float(radius ** 2 * math.pi)

if __name__ == '__main__':
    sample_radius = 5.0
    result = compute_circle_area(sample_radius)
    print(result)