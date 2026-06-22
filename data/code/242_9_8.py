import math

def semicircle_area(radius):
    return 0.5 * math.pi * radius ** 2

def rectangle_area(width, height):
    return width * height

if __name__ == '__main__':
    semicircle_radius = 4
    rectangle_width = 6
    rectangle_height = 3
    
    semicircle_area_value = semicircle_area(semicircle_radius)
    rectangle_area_value = rectangle_area(rectangle_width, rectangle_height)
    
    print("Semicircle area:", semicircle_area_value)
    print("Rectangle area:", rectangle_area_value)