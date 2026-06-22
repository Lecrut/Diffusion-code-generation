import math

def calculate_area(shape, **kwargs):
    area_functions = {
        'circle': lambda r: math.pi * r ** 2,
        'triangle': lambda b, h: 0.5 * b * h
    }
    
    if shape not in area_functions:
        raise ValueError("Invalid shape")
    
    return area_functions[shape](**kwargs)

if __name__ == '__main__':
    circle_radius = 3
    triangle_base = 6
    triangle_height = 2
    
    try:
        circle_area = calculate_area('circle', r=circle_radius)
        print(circle_area)
        
        triangle_area = calculate_area('triangle', b=triangle_base, h=triangle_height)
        print(triangle_area)
    except ValueError as e:
        print(e)