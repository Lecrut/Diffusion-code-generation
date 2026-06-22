class SumCalculator:
    def calculate(self, x: int, y: int) -> int:
        return x + y

if __name__ == '__main__':
    calc = SumCalculator()
    result = calc.calculate(5, 3)
    print(result)