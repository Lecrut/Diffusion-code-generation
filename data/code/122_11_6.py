class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_values = (5, 10, 15, 20)
    print(f"Average of {sample_values}: {calculator.calculate_average(sample_values)}")