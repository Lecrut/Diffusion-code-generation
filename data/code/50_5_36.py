class NonNegativeDifference:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def calculate(x, y):
        return abs(x - y)

if __name__ == '__main__':
    calculator = NonNegativeDifference(50, 25)
    print(calculator.calculate(calculator.x, calculator.y))