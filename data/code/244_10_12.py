import math

PI = 3.14159

def circle_area(radius):
    return PI * radius ** 2

def rectangle_area(width, height):
    return width * height

if __name__ == '__main__':
    circle_radius = 5
    rectangle_width = 10
    rectangle_height = 7
    
    circle_area_result = circle_area(circle_radius)
    rectangle_area_result = rectangle_area(rectangle_width, rectangle_height)
    
    total_area = circle_area_result + rectangle_area_result
    print(total_area)