import math

def square_pyramid_surface_area(base_side, height):
    apothem = math.sqrt(height**2 + (base_side / 2)**2)
    slant_area = base_side * math.sqrt((base_side / 2)**2 + height**2)
    base_area = base_side ** 2
    return base_area + slant_area

if __name__ == '__main__':
    base_side_value = 10.0
    height_value = 12.0
    result = square_pyramid_surface_area(base_side_value, height_value)
    print(result)