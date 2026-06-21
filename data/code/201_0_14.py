class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return None
        total = sum(numbers)
        count = len(numbers)
        mean = total / count
        return mean

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    calculator = AverageCalculator()
    print(calculator.calculate_average(sample_values))