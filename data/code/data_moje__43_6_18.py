import math

def surface_area_of_square_pyramid(base_length, slant_height):
    base_area = base_length ** 2
    lateral_area = 2 * base_length * slant_height
    total_area = base_area + lateral_area
    return total_area

def total_surface_area_of_square_pyramid(base_length, height):
    half_base = base_length / 2
    slant_height = math.sqrt(half_base ** 2 + height ** 2)
    return surface_area_of_square_pyramid(base_length, slant_height)

if __name__ == '__main__':
    base = 10
    height = 12
    result = total_surface_area_of_square_pyramid(base, height)
    print(result)