class StatisticsCalculator:
    def get_mean(self, data):
        if not data:
            return 0
        return sum(data) / len(data)
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_data = [10, 20, 30, 40, 50]
    mean_value = calculator.get_mean(sample_data)
    print(mean_value)