import math

def calculate_area(shape, **kwargs):
    if shape == 'circle':
        radius = kwargs.get('radius')
        area_metric = math.pi * (radius ** 2)
        area_imperial = area_metric * 0.157473
        return area_metric, area_imperial
    elif shape == 'rectangle':
        length = kwargs.get('length')
        width = kwargs.get('width')
        area_metric = length * width
        area_imperial = area_metric * 0.00625
        return area_metric, area_imperial
    elif shape == 'triangle':
        base = kwargs.get('base')
        height = kwargs.get('height')
        area_metric = 0.5 * base * height
        area_imperial = area_metric * 0.155038
        return area_metric, area_imperial
    else:
        raise ValueError("Invalid shape")

if __name__ == '__main__':
    circle_area = calculate_area('circle', radius=5)
    print(f"Circle Area (Metric): {circle_area[0]}, Imperial: {circle_area[1]}")
    
    rectangle_area = calculate_area('rectangle', length=10, width=5)
    print(f"Rectangle Area (Metric): {rectangle_area[0]}, Imperial: {rectangle_area[1]}")
    
    triangle_area = calculate_area('triangle', base=8, height=6)
    print(f"Triangle Area (Metric): {triangle_area[0]}, Imperial: {triangle_area[1]}")