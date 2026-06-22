import math

def calculate_rectangular_prism_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    result = calculate_rectangular_prism_surface_area(1.5, 2.0, 3.0)
    print(result)