class SumCalculator:
    def calculate_sum(self, start, end):
        return (end - start + 1) * (start + end) // 2

if __name__ == '__main__':
    calculator = SumCalculator()
    print(calculator.calculate_sum(1, 10))
    print(calculator.calculate_sum(5, 15))