import math
PI = math.pi

def calculate_circle_perimeter(radius):
    return 2 * PI * radius
if __name__ == '__main__':
    sample_radius_1 = 4
    sample_radius_2 = 9
    perimeter_1 = calculate_circle_perimeter(sample_radius_1)
    print(perimeter_1)
    perimeter_2 = calculate_circle_perimeter(sample_radius_2)
    print(perimeter_2)