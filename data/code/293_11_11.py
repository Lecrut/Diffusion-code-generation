import math

def calculate_area(shape, **kwargs):
    if shape == 'circle':
        radius = kwargs.get('radius', 0)
        area_metric = math.pi * radius ** 2
        area_imperial = area_metric * 15.4986
        return f'Circle: Metric - {area_metric:.2f} m², Imperial - {area_imperial:.2f} sq ft'
    elif shape == 'rectangle':
        length = kwargs.get('length', 0)
        width = kwargs.get('width', 0)
        area_metric = length * width
        area_imperial = area_metric * 10.7639
        return f'Rectangle: Metric - {area_metric:.2f} m², Imperial - {area_imperial:.2f} sq ft'
    elif shape == 'triangle':
        base = kwargs.get('base', 0)
        height = kwargs.get('height', 0)
        area_metric = 0.5 * base * height
        area_imperial = area_metric * 10.7639
        return f'Triangle: Metric - {area_metric:.2f} m², Imperial - {area_imperial:.2f} sq ft'
    else:
        return 'Invalid shape'
if __name__ == '__main__':
    print(calculate_area('circle', radius=5))
    print(calculate_area('rectangle', length=10, width=5))
    print(calculate_area('triangle', base=6, height=4))