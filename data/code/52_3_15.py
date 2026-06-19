import math

def calculate_area(shape, *args):
    area_calculators = {
        'rectangle': lambda length, width: length * width,
        'circle': lambda radius: math.pi * (radius ** 2),
        'triangle': lambda base, height: 0.5 * base * height
    }
    
    if shape in area_calculators:
        return area_calculators[shape](*args)
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', 6, 4)
    circle_area = calculate_area('circle', 3)
    triangle_area = calculate_area('triangle', 8, 5)
    print(f"Rectangle area: {rectangle_area}")
    print(f"Circle area: {circle_area}")
    print(f"Triangle area: {triangle_area}")