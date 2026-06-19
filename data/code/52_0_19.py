class ShapeCalculator:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    sample_base = 7.5
    sample_height = 4.2
    calculator = ShapeCalculator(sample_base, sample_height)
    
    area_result = calculator.calculate_area()
    print(area_result)

    another_base = 10.0
    another_height = 3.5
    calculator.base = another_base
    calculator.height = another_height
    
    another_area_result = calculator.calculate_area()
    print(another_area_result)