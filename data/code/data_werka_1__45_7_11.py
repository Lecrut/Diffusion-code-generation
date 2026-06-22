import math

def calculate_circle_area(radius):
    pi_value = math.pi
    area = pi_value * radius ** 2
    return area

if __name__ == '__main__':
    sample_radius = 3.5
    circle_area = calculate_circle_area(sample_radius)
    print(circle_area)