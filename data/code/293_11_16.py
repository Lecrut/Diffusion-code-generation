import math

def calculate_area(shape, **kwargs):
    if shape == 'circle':
        radius = kwargs['radius']
        area_metric = math.pi * radius ** 2
        area_imperial = area_metric * 10.7639
        return area_metric, area_imperial
    elif shape == 'rectangle':
        length = kwargs['length']
        width = kwargs['width']
        area_metric = length * width
        area_imperial = area_metric * 10.7639
        return area_metric, area_imperial
    elif shape == 'triangle':
        base = kwargs['base']
        height = kwargs['height']
        area_metric = 0.5 * base * height
        area_imperial = area_metric * 10.7639
        return area_metric, area_imperial
    else:
        raise ValueError("Invalid shape")

if __name__ == '__main__':
    circle_area = calculate_area('circle', radius=5)
    print(f"Circle area (metric): {circle_area[0]}, (imperial): {circle_area[1]}")
    
    rectangle_area = calculate_area('rectangle', length=4, width=3)
    print(f"Rectangle area (metric): {rectangle_area[0]}, (imperial): {rectangle_area[1]}")
    
    triangle_area = calculate_area('triangle', base=6, height=4)
    print(f"Triangle area (metric): {triangle_area[0]}, (imperial): {triangle_area[1]}")