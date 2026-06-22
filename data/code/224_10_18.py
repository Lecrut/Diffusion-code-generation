class StatisticsCalculator:
    @staticmethod
    def calculate_mean(numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5]
    mean_value = StatisticsCalculator.calculate_mean(sample_values)
    print(f"Mean of {sample_values}: {mean_value}")