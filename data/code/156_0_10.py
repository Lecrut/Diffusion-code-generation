class StatisticsCalculator:
    def calculate_average(self, numbers):
        if not numbers:
            return None
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_values = [10, 20, 30, 40, 50]
    avg_value = calculator.calculate_average(sample_values)
    print(avg_value)