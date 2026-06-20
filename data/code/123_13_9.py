class SumCalculator:
    def calculate_sum(self, start, end):
        return sum(i for i in range(start, end + 1))

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum(1, 100)
    print(result)