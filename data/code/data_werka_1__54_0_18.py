import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius_large = 10
    area_large = calculate_circle_area(sample_radius_large)
    print(f"The area of a circle with large radius ({sample_radius_large}) is: {area_large}")

    sample_radius_small = 2
    area_small = calculate_circle_area(sample_radius_small)
    print(f"The area of a circle with small radius ({sample_radius_small}) is: {area_small}")