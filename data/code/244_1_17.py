class ShapeCalculator:
    def calculate_area(self, shape_type, *params):
        if shape_type == 'rectangle':
            return params[0] * params[1]
        elif shape_type == 'triangle':
            base, height = params
            return 0.5 * base * height

if __name__ == '__main__':
    calculator = ShapeCalculator()
    rectangle_area = calculator.calculate_area('rectangle', 10, 6)
    triangle_area = calculator.calculate_area('triangle', 8, 5)
    total_area = rectangle_area + triangle_area
    print(total_area)