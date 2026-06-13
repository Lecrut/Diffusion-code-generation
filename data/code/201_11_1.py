class StatisticsCalculator:
    def get_average(self, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_data = [10, 20, 30, 40, 50]
    average = calculator.get_average(sample_data)
    print(average)