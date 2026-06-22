class SumCalculator:
    def add_numbers(self, a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    calculator = SumCalculator()
    result1 = calculator.add_numbers(15, 27)
    result2 = calculator.add_numbers(3, 5)
    print(result1)
    print(result2)