class SquareCalculator:
    def __init__(self, side):
        self.side = side

    def compute(self):
        if self.side < 0:
            return 0
        return self.side * self.side

if __name__ == '__main__':
    CALCULATOR = SquareCalculator(7)
    print(CALCULATOR.compute())