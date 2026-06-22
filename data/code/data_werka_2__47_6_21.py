def calculate_area(shape, **kwargs):
    if shape == 'rectangle':
        return kwargs['length'] * kwargs['width']
    elif shape == 'circle':
        import math
        return math.pi * (kwargs['radius'] ** 2)
    elif shape == 'triangle':
        return 0.5 * kwargs['base'] * kwargs['height']
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    print(calculate_area('rectangle', length=5, width=3))
    print(calculate_area('circle', radius=4))
    print(calculate_area('triangle', base=6, height=2))