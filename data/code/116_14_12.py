class SumCalculator:
    @staticmethod
    def add_numbers(a: int, b: int) -> int:
        return a + b

    def sum_three(self, a: int, b: int, c: int) -> int:
        return self.add_numbers(SumCalculator.add_numbers(a, b), c)

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.sum_three(10, 20, 30)
    print(result)