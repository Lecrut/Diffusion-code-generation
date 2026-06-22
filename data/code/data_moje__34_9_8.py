import math

PI_CONSTANT = math.pi

def cylinder_surface_area(radius, height):
    two_pi = 2 * PI_CONSTANT
    base_area_contribution = two_pi * radius ** 2
    lateral_area_contribution = two_pi * radius * height
    return base_area_contribution + lateral_area_contribution

if __name__ == '__main__':
    SAMPLE_RADIUS = 7.5
    SAMPLE_HEIGHT = 12.0
    calculated_area = cylinder_surface_area(SAMPLE_RADIUS, SAMPLE_HEIGHT)
    print(calculated_area)