class AverageCalculator:
    @staticmethod
    def calculate_mean(numbers):
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_values = [5, 10, 15, 20]
    result = calculator.calculate_mean(sample_values)
    print(result)