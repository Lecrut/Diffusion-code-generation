import math

def calculate_area(shape_type, dimensions):
    area_calculators = {
        'circle': lambda r: math.pi * r ** 2,
        'rectangle': lambda l, w: l * w,
        'triangle': lambda b, h: 0.5 * b * h
    }
    
    if shape_type in area_calculators:
        return area_calculators[shape_type](*dimensions)
    else:
        raise ValueError("Invalid shape type")

if __name__ == '__main__':
    radius = 5
    circle_area = calculate_area('circle', (radius,))
    print(circle_area)