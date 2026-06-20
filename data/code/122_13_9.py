class StatisticsCalculator:
    @staticmethod
    def calculate_mean(numbers):
        if not numbers:
            raise ValueError("The list of numbers cannot be empty.")
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 6.7]
    calculator = StatisticsCalculator()
    try:
        mean = calculator.calculate_mean(sample_numbers)
        print(mean)
    except ValueError as e:
        print(e)