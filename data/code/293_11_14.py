import math

def calculate_area(shape, **kwargs):
    if shape == 'circle':
        radius = kwargs.get('radius', 0)
        area_metric = math.pi * radius ** 2
        area_imperial = area_metric * 15.4986
        return (area_metric, area_imperial)
    elif shape == 'rectangle':
        length = kwargs.get('length', 0)
        width = kwargs.get('width', 0)
        area_metric = length * width
        area_imperial = area_metric * 10.7639
        return (area_metric, area_imperial)
    elif shape == 'triangle':
        base = kwargs.get('base', 0)
        height = kwargs.get('height', 0)
        area_metric = 0.5 * base * height
        area_imperial = area_metric * 10.7639
        return (area_metric, area_imperial)
    else:
        raise ValueError('Unsupported shape')
if __name__ == '__main__':
    circle_area = calculate_area('circle', radius=5)
    rectangle_area = calculate_area('rectangle', length=10, width=5)
    triangle_area = calculate_area('triangle', base=8, height=6)
    print(f'Circle area (metric): {circle_area[0]}, (imperial): {circle_area[1]}')
    print(f'Rectangle area (metric): {rectangle_area[0]}, (imperial): {rectangle_area[1]}')
    print(f'Triangle area (metric): {triangle_area[0]}, (imperial): {triangle_area[1]}')