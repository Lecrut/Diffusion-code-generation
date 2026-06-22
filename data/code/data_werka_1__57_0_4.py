import math

def calculate_area_circle(radius):
    area = math.pi * radius ** 2
    return area

if __name__ == '__main__':
    test_radius = 7.5
    computed_area = calculate_area_circle(test_radius)
    print(computed_area)