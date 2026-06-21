class StatisticsCalculator:
    @staticmethod
    def calculate_mean(data):
        if not data:
            return None
        total_sum = sum(data)
        count = len(data)
        mean_value = total_sum / count
        return mean_value

if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_data = [10, 20, 30, 40, 50]
    mean_value = calculator.calculate_mean(sample_data)
    print(mean_value)