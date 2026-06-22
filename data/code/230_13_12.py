class CumulativeSumCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate(self):
        return tuple(sum(self.numbers[:i+1]) for i in range(len(self.numbers)))

if __name__ == '__main__':
    calculator = CumulativeSumCalculator((1, 2, 3, 4, 5))
    print(calculator.calculate())