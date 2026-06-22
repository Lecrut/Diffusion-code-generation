import math

def ellipse_area(semi_major, semi_minor):
    return math.pi * semi_major * semi_minor

def rectangle_area(width, height):
    return width * height

def compare_areas(semi_major, semi_minor, width, height):
    ellipse = ellipse_area(semi_major, semi_minor)
    rectangle = rectangle_area(width, height)
    
    if ellipse > rectangle:
        return "Ellipse is larger"
    elif ellipse < rectangle:
        return "Rectangle is larger"
    else:
        return "Areas are equal"

if __name__ == '__main__':
    print(compare_areas(5, 3, 10, 6))