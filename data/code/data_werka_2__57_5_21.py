import math

def calculate_area(shape, **kwargs):
    area_calculators = {
        'square': lambda side: side * side,
        'circle': lambda radius: math.pi * radius * radius,
    }
    
    if shape not in area_calculators:
        raise ValueError(f"Unsupported shape: {shape}")
    
    return area_calculators[shape](**kwargs)

if __name__ == '__main__':
    square_area = calculate_area('square', side=5)
    circle_area = calculate_area('circle', radius=3)
    
    print(f"Area of square with side 5: {square_area}")
    print(f"Area of circle with radius 3: {circle_area}")