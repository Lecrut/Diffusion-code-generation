import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius * radius

if __name__ == '__main__':
    sample_radius_1 = 5
    sample_radius_2 = 10.5
    result_1 = calculate_circle_area(sample_radius_1)
    result_2 = calculate_circle_area(sample_radius_2)
    print(result_1)
    print(result_2)