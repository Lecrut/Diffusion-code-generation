import math

def square_pyramid_surface_area(base_length, height):
    slant_height = math.sqrt((base_length / 2) ** 2 + height ** 2)
    base_area = base_length ** 2
    lateral_area = 2 * base_length * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base = 4.0
    height = 6.0
    result = square_pyramid_surface_area(base, height)
    print(result)