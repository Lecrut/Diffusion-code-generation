import math

def calculate_area(shape, **kwargs):
    area_calculators = {
        'square': lambda side: side * side,
        'circle': lambda radius: math.pi * radius * radius,
    }
    
    if shape in area_calculators:
        calculator = area_calculators[shape]
        return calculator(**kwargs)
    else:
        raise ValueError(f"Unsupported shape: {shape}")

if __name__ == '__main__':
    square_side_length = 7
    circle_radius = 4
    
    square_area_result = calculate_area('square', side=square_side_length)
    circle_area_result = calculate_area('circle', radius=circle_radius)
    
    print(f"Area of square with side {square_side_length}: {square_area_result}")
    print(f"Area of circle with radius {circle_radius}: {circle_area_result}")