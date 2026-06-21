class StatisticsCalculator:
    @staticmethod
    def calculate_mean(numbers):
        if not numbers:
            return 0
        total_sum = sum(numbers)
        count = len(numbers)
        mean = total_sum / count
        return mean

if __name__ == '__main__':
    sample_numbers = [10.5, 20.3, 30.7, 40.2, 50.8, 60.1, 70.9, 80.4, 90.6, 100.2]
    mean_value = StatisticsCalculator.calculate_mean(sample_numbers)
    print(f"The mean of the numbers is: {mean_value}")