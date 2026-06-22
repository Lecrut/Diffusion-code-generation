class FactorialCalculator:
    def __init__(self, base: int):
        self.base = base

    def compute(self) -> int:
        result = 1
        for index in range(1, self.base + 1):
            result *= index
        return result

if __name__ == '__main__':
    calculator = FactorialCalculator(20)
    print(calculator.compute())