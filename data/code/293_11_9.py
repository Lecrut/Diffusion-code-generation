import math

def calculate_area(shape, **kwargs):
    if shape == 'circle':
        radius = kwargs['radius']
        area_metric = math.pi * radius ** 2
        area_imperial = area_metric * 0.157473644
        return (area_metric, area_imperial)
    elif shape == 'rectangle':
        length = kwargs['length']
        width = kwargs['width']
        area_metric = length * width
        area_imperial = area_metric * 10.7639104
        return (area_metric, area_imperial)
    elif shape == 'triangle':
        base = kwargs['base']
        height = kwargs['height']
        area_metric = 0.5 * base * height
        area_imperial = area_metric * 10.7639104
        return (area_metric, area_imperial)
    else:
        raise ValueError('Unsupported shape')
if __name__ == '__main__':
    circle_area = calculate_area('circle', radius=5)
    print(f'Circle Area (Metric): {circle_area[0]}, Circle Area (Imperial): {circle_area[1]}')
    rectangle_area = calculate_area('rectangle', length=10, width=5)
    print(f'Rectangle Area (Metric): {rectangle_area[0]}, Rectangle Area (Imperial): {rectangle_area[1]}')
    triangle_area = calculate_area('triangle', base=7, height=4)
    print(f'Triangle Area (Metric): {triangle_area[0]}, Triangle Area (Imperial): {triangle_area[1]}')