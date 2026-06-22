import math

def square_pyramid_surface_area(base_side, height):
    half_base = base_side / 2.0
    slant_height = math.sqrt(height**2 + half_base**2)
    base_area = base_side**2
    lateral_area = base_side * math.sqrt((height**2 + (base_side / 2.0)**2)) * 2.0
    return base_area + lateral_area

if __name__ == '__main__':
    side = 4.0
    h = 3.0
    area = square_pyramid_surface_area(side, h)
    print(area)