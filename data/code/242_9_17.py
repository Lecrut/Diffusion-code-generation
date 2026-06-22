import math

def semicircle_area(radius):
    return 0.5 * math.pi * radius ** 2

def rectangle_area(width, height):
    return width * height

if __name__ == '__main__':
    radius = 4
    width = 6
    height = 3
    
    semicircle_result = semicircle_area(radius)
    rectangle_result = rectangle_area(width, height)
    
    print(f"Semicircle area: {semicircle_result}")
    print(f"Rectangle area: {rectangle_result}")