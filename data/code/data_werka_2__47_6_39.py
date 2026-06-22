import math
PI = math.pi

def calculate_area(shape, **kwargs):
    return {'rectangle': kwargs['length'] * kwargs['width'], 'circle': PI * kwargs['radius'] ** 2, 'triangle': 0.5 * kwargs['base'] * kwargs['height']}.get(shape.lower(), lambda: None)()
if __name__ == '__main__':
    print(calculate_area('rectangle', length=5, width=3))
    print(calculate_area('circle', radius=4))
    print(calculate_area('triangle', base=6, height=2))