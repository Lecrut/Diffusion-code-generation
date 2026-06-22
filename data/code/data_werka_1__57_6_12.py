import math

def calculate_area(shape, **kwargs):
    area_calculators = {
        'square': lambda side: side * side,
        'circle': lambda radius: math.pi * radius * radius,
    }
    
    if shape not in area_calculators:
        raise ValueError(f"Unsupported shape: {shape}")
    
    calculator = area_calculators[shape]
    return calculator(**kwargs)

if __name__ == '__main__':
    try:
        square_side = 7.5
        circle_radius = 2.8
        square_area = calculate_area('square', side=square_side)
        circle_area = calculate_area('circle', radius=circle_radius)
        
        print(f"Area of square with side {square_side}: {square_area}")
        print(f"Area of circle with radius {circle_radius}: {circle_area}")
    except ValueError as e:
        print(e)