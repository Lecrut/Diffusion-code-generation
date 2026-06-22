class ShapeCalculator:

    def area_circle(self, radius: float) -> dict[str, float]:
        pi = 3.14159
        metric_area = pi * radius ** 2
        imperial_area = metric_area * 0.764538
        return {'metric': metric_area, 'imperial': imperial_area}

    def area_rectangle(self, length: float, width: float) -> dict[str, float]:
        metric_area = length * width
        imperial_area = metric_area * 10.7639
        return {'metric': metric_area, 'imperial': imperial_area}

    def area_triangle(self, base: float, height: float) -> dict[str, float]:
        metric_area = base * height / 2
        imperial_area = metric_area * 10.7639
        return {'metric': metric_area, 'imperial': imperial_area}
if __name__ == '__main__':
    calculator = ShapeCalculator()
    circle_result = calculator.area_circle(5)
    print(f'Circle - Metric: {circle_result['metric']}, Imperial: {circle_result['imperial']}')
    rectangle_result = calculator.area_rectangle(10, 5)
    print(f'Rectangle - Metric: {rectangle_result['metric']}, Imperial: {rectangle_result['imperial']}')
    triangle_result = calculator.area_triangle(8, 6)
    print(f'Triangle - Metric: {triangle_result['metric']}, Imperial: {triangle_result['imperial']}')