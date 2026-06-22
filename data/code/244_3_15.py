class ShapeCalculator:
    def trapezoid_area(self, base1, base2, height):
        return 0.5 * (base1 + base2) * height
    
    def parallelogram_area(self, base, height):
        return base * height

if __name__ == '__main__':
    calculator = ShapeCalculator()
    trapezoid = calculator.trapezoid_area(5, 7, 4)
    parallelogram = calculator.parallelogram_area(6, 3)
    print(trapezoid + parallelogram)