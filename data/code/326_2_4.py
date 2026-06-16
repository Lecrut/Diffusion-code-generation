class StatisticsCalculator:
    def compute_average(self, numbers):
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_list = [10.5, 20.5, 30.0, 40.0, 5.5]
    average = calculator.compute_average(sample_list)
    print(average)