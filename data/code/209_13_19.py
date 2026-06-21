class AverageCalculator:
    DEFAULT_VALUE = 0

    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return AverageCalculator.DEFAULT_VALUE
        total = sum(numbers)
        count = len(numbers)
        return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    calculator = AverageCalculator()
    result = calculator.calculate_average(sample_values)
    print(result)