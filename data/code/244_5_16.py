import math

def semicircle_area(radius):
    return 0.5 * math.pi * (radius ** 2)

def rectangle_area(length, width):
    return length * width

if __name__ == '__main__':
    semicircle_radius = 4
    rectangle_length = 6
    rectangle_width = 9
    
    semicircle_result = semicircle_area(semicircle_radius)
    rectangle_result = rectangle_area(rectangle_length, rectangle_width)
    
    total_area = semicircle_result + rectangle_result
    print(total_area)