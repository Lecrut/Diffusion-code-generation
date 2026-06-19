import math

def calculate_circle_area(radius):
    pi_value = 3.141592653589793
    area = pi_value * radius ** 2
    return area

if __name__ == '__main__':
    sample_radius = 3.0
    calculated_area = calculate_circle_area(sample_radius)
    print(calculated_area)