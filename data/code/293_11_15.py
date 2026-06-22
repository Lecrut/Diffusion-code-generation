PI = 3.141592653589793
SQRT_3 = 1.7320508075688772

def calculate_circle_area(radius: float) -> dict:
    metric_area = PI * radius ** 2
    imperial_area = metric_area / 0.000645744
    return {'metric': metric_area, 'imperial': imperial_area}

def calculate_rectangle_area(length: float, width: float) -> dict:
    metric_area = length * width
    imperial_area = metric_area / 0.000645744
    return {'metric': metric_area, 'imperial': imperial_area}

def calculate_triangle_area(base: float, height: float) -> dict:
    metric_area = 0.5 * base * height
    imperial_area = metric_area / 0.000645744
    return {'metric': metric_area, 'imperial': imperial_area}
if __name__ == '__main__':
    circle_result = calculate_circle_area(1)
    rectangle_result = calculate_rectangle_area(2, 3)
    triangle_result = calculate_triangle_area(4, 5)
    print(f'Circle area: Metric - {circle_result['metric']}, Imperial - {circle_result['imperial']}')
    print(f'Rectangle area: Metric - {rectangle_result['metric']}, Imperial - {rectangle_result['imperial']}')
    print(f'Triangle area: Metric - {triangle_result['metric']}, Imperial - {triangle_result['imperial']}')