import math

def semicircle_area(radius):
    return 0.5 * math.pi * radius ** 2

def rectangle_area(width, height):
    return width * height

if __name__ == '__main__':
    shapes = {
        'semicircle': {'radius': 4},
        'rectangle': {'width': 6, 'height': 3}
    }
    
    areas = {}
    for shape, params in shapes.items():
        if shape == 'semicircle':
            areas[shape] = semicircle_area(params['radius'])
        elif shape == 'rectangle':
            areas[shape] = rectangle_area(params['width'], params['height'])
    
    print(f"Semicircle area: {areas['semicircle']:.10f}")
    print(f"Rectangle area: {areas['rectangle']:.10f}")