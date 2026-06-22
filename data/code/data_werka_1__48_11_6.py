import math

def validate_dimensions(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers.")
    return True

def calculate_perimeter(width, height):
    return 2 * (width + height)

def calculate_area(width, height):
    return width * height

if __name__ == '__main__':
    width = 5.0
    height = 3.0
    
    try:
        if validate_dimensions(width, height):
            perimeter = calculate_perimeter(width, height)
            area = calculate_area(width, height)
            print(f"Perimeter: {perimeter}")
            print(f"Area: {area}")
    except ValueError as e:
        print(e)