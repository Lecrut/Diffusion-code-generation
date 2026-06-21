import math

def calculate_area(shape, **kwargs):
    area_calculators = {
        'square': lambda side: side * side,
        'circle': lambda radius: math.pi * radius * radius,
    }
    
    if shape in area_calculators:
        return area_calculators[shape](**kwargs)
    else:
        raise ValueError(f"Unsupported shape: {shape}")

if __name__ == '__main__':
    square_area = calculate_area('square', side=5)
    circle_area = calculate_area('circle', radius=3)
    
    print(f"Area of the square: {square_area}")
    print(f"Area of the circle: {circle_area}")