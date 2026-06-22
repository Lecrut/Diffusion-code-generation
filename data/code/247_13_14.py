class SumCalculator:
    def calculate_sum(self, x: int, y: int) -> int:
        return x + y

if __name__ == '__main__':
    calculator = SumCalculator()
    result1 = calculator.calculate_sum(5, 3)
    result2 = calculator.calculate_sum(-10, 15)
    print(result1)
    print(result2)