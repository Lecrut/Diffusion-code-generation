class SumCalculator:
    def calculate_sum(self, numbers):
        return sum(numbers)

if __name__ == '__main__':
    calculator = SumCalculator()
    print(calculator.calculate_sum([10, 20, 35, 42]))
    print(calculator.calculate_sum([]))