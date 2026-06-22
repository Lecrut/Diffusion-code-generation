class SumCalculator:
    def calculate_sum(self, x: int, y: int) -> int:
        return x + y

if __name__ == '__main__':
    calc = SumCalculator()
    result1 = calc.calculate_sum(5, 3)
    print(result1)
    result2 = calc.calculate_sum(-10, 20)
    print(result2)