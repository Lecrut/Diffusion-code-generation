class StatisticsCalculator:
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return None
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    avg_value = StatisticsCalculator.calculate_average(sample_values)
    print(avg_value)