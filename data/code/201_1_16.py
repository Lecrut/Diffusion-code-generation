import statistics

class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return 0
        return statistics.mean(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_numbers = [10, 20, 30, 40, 50]
    print(f"Average: {calculator.calculate_average(sample_numbers)}")