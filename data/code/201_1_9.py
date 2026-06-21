import statistics

class AverageCalculator:
    def calculate_average(self, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_numbers = [10, 20, 30, 40, 50]
    print(f"Average of sample_numbers: {calculator.calculate_average(sample_numbers)}")