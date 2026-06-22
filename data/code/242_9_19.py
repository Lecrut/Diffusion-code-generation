import math

def semicircle_area(radius):
    return 0.5 * math.pi * radius ** 2

def rectangle_area(width, height):
    return width * height

if __name__ == '__main__':
    radius = 4
    width = 6
    height = 3
    
    semicircle_a = semicircle_area(radius)
    rectangle_a = rectangle_area(width, height)
    
    print(f"Semicircle area: {semicircle_a}")
    print(f"Rectangle area: {rectangle_a}")