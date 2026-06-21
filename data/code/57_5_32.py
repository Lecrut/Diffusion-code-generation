import math

def calculate_area(shape, **kwargs):
    def square(side):
        return side * side
    
    def circle(radius):
        return math.pi * radius * radius
    
    area_calculators = {
        'square': square,
        'circle': circle,
    }
    
    if shape not in area_calculators:
        raise ValueError(f"Unsupported shape: {shape}")
    
    calculator = area_calculators[shape]
    return calculator(**kwargs)

if __name__ == '__main__':
    try:
        side_length = 8
        square_area_result = calculate_area('square', side=side_length)
        radius_length = 2
        circle_area_result = calculate_area('circle', radius=radius_length)
        
        print(f"Area of square with side {side_length}: {square_area_result}")
        print(f"Area of circle with radius {radius_length}: {circle_area_result}")
    except ValueError as e:
        print(e)