import math

def calculate_area(shape):
    shape_type = shape.get('type')
    area_calculators = {
        'rectangle': lambda params: params['width'] * params['height'],
        'circle': lambda params: math.pi * (params['radius'] ** 2),
        'triangle': lambda params: 0.5 * params['base'] * params['height']
    }
    
    if shape_type in area_calculators:
        return area_calculators[shape_type](shape)
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    rectangle = {'type': 'rectangle', 'width': 3, 'height': 6}
    circle = {'type': 'circle', 'radius': 4}
    triangle = {'type': 'triangle', 'base': 10, 'height': 2}
    
    print("Rectangle area:", calculate_area(rectangle))
    print("Circle area:", calculate_area(circle))
    print("Triangle area:", calculate_area(triangle))