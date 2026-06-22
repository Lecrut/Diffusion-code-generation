import math

def calculate_area_circle(radius):
    area = math.pi * radius ** 2
    return area

if __name__ == '__main__':
    sample_radius_value = 7.0
    computed_area = calculate_area_circle(sample_radius_value)
    print(computed_area)