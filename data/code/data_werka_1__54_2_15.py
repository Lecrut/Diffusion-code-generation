import math
PI = math.pi

def get_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radius_1 = 5.0
    sample_radius_2 = 10.5
    area_1 = get_area(sample_radius_1)
    area_2 = get_area(sample_radius_2)
    print(f'Area of circle with radius {sample_radius_1}: {area_1}')
    print(f'Area of circle with radius {sample_radius_2}: {area_2}')