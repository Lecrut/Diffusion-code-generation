class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        total = sum(numbers)
        count = len(numbers)
        return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_values = [12, 24, 36, 48, 60]
    calculator = AverageCalculator()
    result = calculator.calculate_average(sample_values)
    print(result)