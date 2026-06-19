import math

def compute_circle_perimeter(radius):
    pi_value = math.pi
    diameter = 2 * radius
    perimeter = pi_value * diameter
    return perimeter

if __name__ == '__main__':
    sample_radius = 7.5
    result_perimeter = compute_circle_perimeter(sample_radius)
    print(result_perimeter)