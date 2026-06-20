class SumCalculator:
    def sum_range(self, start: int, end: int) -> int:
        return (end - start + 1) * (start + end) // 2

if __name__ == '__main__':
    calculator = SumCalculator()
    print(calculator.sum_range(1, 10))
    print(calculator.sum_range(5, 15))