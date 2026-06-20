class SumCalculator:
    def calculate_sum(self, start, end):
        return (end * (end + 1)) // 2 - ((start - 1) * start // 2)

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum(1, 1000)
    print(result)