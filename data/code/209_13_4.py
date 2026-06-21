class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        total = sum(numbers)
        count = len(numbers)
        return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    calculator = AverageCalculator()
    result = calculator.calculate_average(sample_values)
    print(result)