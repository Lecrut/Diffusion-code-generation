import math

def calculate_area(shape, **kwargs):
    def square_area(side):
        return side * side
    
    def circle_area(radius):
        return math.pi * radius * radius
    
    area_calculators = {
        'square': square_area,
        'circle': circle_area,
    }
    
    if shape not in area_calculators:
        raise ValueError(f"Unsupported shape: {shape}")
    
    calculator_function = area_calculators[shape]
    return calculator_function(**kwargs)

if __name__ == '__main__':
    try:
        side_length = 8
        square_result = calculate_area('square', side=side_length)
        
        radius_length = 5
        circle_result = calculate_area('circle', radius=radius_length)
        
        print(f"Area of square with side {side_length}: {square_result}")
        print(f"Area of circle with radius {radius_length}: {circle_result}")
    except ValueError as e:
        print(e)