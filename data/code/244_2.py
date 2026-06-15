class Shape:
    def __init__(self, area):
        self.area = area
class ShapeCalculator:
    def calculate_total_area(self, shape1, shape2):
        return shape1.area + shape2.area
if __name__ == '__main__':
    shape_a = Shape(10)
    shape_b = Shape(15)
    calculator = ShapeCalculator()
    total_area = calculator.calculate_total_area(shape_a, shape_b)
    print(total_area)