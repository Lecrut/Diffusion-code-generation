class StatisticsCalculator:
    def get_average(self, data):
        if not data:
            return 0
        return sum(data) / len(data)
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_data = [10, 20, 30, 40, 50]
    average = calculator.get_average(sample_data)
    print(average)