import math
SPHERE_TO_CUBE_RATIO = 0.5236
EPSILON = 1e-09

def calculate_sphere_surface_area(radius):
    return 4 * math.pi * radius ** 2

def calculate_cube_surface_area(side_length):
    return 6 * side_length ** 2

def compare_areas(circle_radius, square_side):
    sphere_area = calculate_sphere_surface_area(circle_radius)
    cube_area = calculate_cube_surface_area(square_side)
    if abs(sphere_area - cube_area) < EPSILON:
        print('The areas are approximately equal.')
    elif sphere_area > cube_area:
        print(f'The sphere area is larger by {sphere_area - cube_area:.2f}.')
    else:
        print(f'The cube area is larger by {cube_area - sphere_area:.2f}.')
if __name__ == '__main__':
    circle_radius = 5.0
    square_side = 5.0
    compare_areas(circle_radius, square_side)