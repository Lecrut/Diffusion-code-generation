class SumCalculator:
    def calculate_total_sum(self, start, end):
        return (end * (end + 1) - start * (start - 1)) // 2

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_total_sum(1, 1000)
    print(result)