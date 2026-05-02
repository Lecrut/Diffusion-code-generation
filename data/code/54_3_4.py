import math
def get_area(radius):
    return math.pi * (radius ** 2)
if __name__ == '__main__':
    sample_radius_1 = 5.0
    area_1 = get_area(sample_radius_1)
    print(f"The area for radius {sample_radius_1} is {area_1}")
    sample_radius_2 = 2.5
    area_2 = get_area(sample_radius_2)
    print(f"The area for radius {sample_radius_2} is {area_2}")
    sample_radius_3 = 0.0
    area_3 = get_area(sample_radius_3)
    print(f"The area for radius {sample_radius_3} is {area_3}")