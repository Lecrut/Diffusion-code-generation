class ShapeCalculator:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        if self.side_length <= 0:
            return 0.0
        return self.side_length ** 2

if __name__ == '__main__':
    calc = ShapeCalculator(4)
    print(calc.area())