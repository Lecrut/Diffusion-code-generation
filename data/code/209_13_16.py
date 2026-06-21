class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    calculator = AverageCalculator()
    result = calculator.calculate_average(sample_values)
    print(result)